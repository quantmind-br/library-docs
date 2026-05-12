---
title: Realtime - vLLM
url: https://docs.vllm.ai/en/latest/examples/speech_to_text/realtime/
source: sitemap
fetched_at: 2026-05-07T21:13:55.413685581-03:00
rendered_js: false
word_count: 13
summary: This document provides example implementations for interacting with the vLLM Realtime WebSocket API to perform speech-to-text transcription using audio files or live microphone input.
tags:
    - vllm
    - speech-to-text
    - websocket-api
    - audio-processing
    - realtime-inference
    - gradio
category: tutorial
---

[](https://github.com/vllm-project/vllm/edit/main/docs/examples/speech_to_text/realtime.md "Edit this page")

Source [https://github.com/vllm-project/vllm/tree/main/examples/speech\_to\_text/realtime](https://github.com/vllm-project/vllm/tree/main/examples/speech_to_text/realtime).

## OpenAI Realtime Client[¶](#openai-realtime-client "Permanent link")

```
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
"""
This script demonstrates how to use the vLLM Realtime WebSocket API to perform
audio transcription by uploading an audio file.

Before running this script, you must start the vLLM server with a realtime-capable
model, for example:

    vllm serve mistralai/Voxtral-Mini-4B-Realtime-2602 --enforce-eager

Requirements:
- vllm with audio support
- websockets
- numpy

The script:
1. Connects to the Realtime WebSocket endpoint
2. Converts an audio file to PCM16 @ 16kHz
3. Sends audio chunks to the server
4. Receives and prints transcription as it streams
"""

importargparse
importasyncio
importjson

importnumpyasnp
importpybase64asbase64
importwebsockets

fromvllm.assets.audioimport AudioAsset
fromvllm.multimodal.media.audioimport load_audio


defaudio_to_pcm16_base64(audio_path: str) -> str:
"""
    Load an audio file and convert it to base64-encoded PCM16 @ 16kHz.
    """
    # Load audio and resample to 16kHz mono
    audio, _ = load_audio(audio_path, sr=16000, mono=True)
    # Convert to PCM16
    pcm16 = (audio * 32767).astype(np.int16)
    # Encode as base64
    return base64.b64encode(pcm16.tobytes()).decode("utf-8")


async defrealtime_transcribe(audio_path: str, host: str, port: int, model: str):
"""
    Connect to the Realtime API and transcribe an audio file.
    """
    uri = f"ws://{host}:{port}/v1/realtime"

    async with websockets.connect(uri) as ws:
        # Wait for session.created
        response = json.loads(await ws.recv())
        if response["type"] == "session.created":
            print(f"Session created: {response['id']}")
        else:
            print(f"Unexpected response: {response}")
            return

        # Validate model
        await ws.send(json.dumps({"type": "session.update", "model": model}))

        # Signal ready to start
        await ws.send(json.dumps({"type": "input_audio_buffer.commit"}))

        # Convert audio file to base64 PCM16
        print(f"Loading audio from: {audio_path}")
        audio_base64 = audio_to_pcm16_base64(audio_path)

        # Send audio in chunks (4KB of raw audio = ~8KB base64)
        chunk_size = 4096
        audio_bytes = base64.b64decode(audio_base64)
        total_chunks = (len(audio_bytes) + chunk_size - 1) // chunk_size

        print(f"Sending {total_chunks} audio chunks...")
        for i in range(0, len(audio_bytes), chunk_size):
            chunk = audio_bytes[i : i + chunk_size]
            await ws.send(
                json.dumps(
                    {
                        "type": "input_audio_buffer.append",
                        "audio": base64.b64encode(chunk).decode("utf-8"),
                    }
                )
            )

        # Signal all audio is sent
        await ws.send(json.dumps({"type": "input_audio_buffer.commit", "final": True}))
        print("Audio sent. Waiting for transcription...\n")

        # Receive transcription
        print("Transcription: ", end="", flush=True)
        while True:
            response = json.loads(await ws.recv())
            if response["type"] == "transcription.delta":
                print(response["delta"], end="", flush=True)
            elif response["type"] == "transcription.done":
                print(f"\n\nFinal transcription: {response['text']}")
                if response.get("usage"):
                    print(f"Usage: {response['usage']}")
                break
            elif response["type"] == "error":
                print(f"\nError: {response['error']}")
                break


defmain(args):
    if args.audio_path:
        audio_path = args.audio_path
    else:
        # Use default audio asset
        audio_path = str(AudioAsset("mary_had_lamb").get_local_path())
        print(f"No audio path provided, using default: {audio_path}")

    asyncio.run(realtime_transcribe(audio_path, args.host, args.port, args.model))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Realtime WebSocket Transcription Client"
    )
    parser.add_argument(
        "--model",
        type=str,
        default="mistralai/Voxtral-Mini-4B-Realtime-2602",
        help="Model that is served and should be pinged.",
    )
    parser.add_argument(
        "--audio_path",
        type=str,
        default=None,
        help="Path to the audio file to transcribe.",
    )
    parser.add_argument(
        "--host",
        type=str,
        default="localhost",
        help="vLLM server host (default: localhost)",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=8000,
        help="vLLM server port (default: 8000)",
    )
    args = parser.parse_args()
    main(args)
```

## OpenAI Realtime Microphone Client[¶](#openai-realtime-microphone-client "Permanent link")

```
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
"""
Minimal Gradio demo for real-time speech transcription using the vLLM Realtime API.

Start the vLLM server first:

    vllm serve mistralai/Voxtral-Mini-4B-Realtime-2602 --enforce-eager

Then run this script:

    python openai_realtime_microphone_client.py --host localhost --port 8000

Use --share to create a public Gradio link.

Requirements: websockets, numpy, gradio
"""

importargparse
importasyncio
importjson
importqueue
importthreading

importgradioasgr
importnumpyasnp
importpybase64asbase64
importwebsockets

SAMPLE_RATE = 16_000

# Global state
audio_queue: queue.Queue = queue.Queue()
transcription_text = ""
is_running = False
ws_url = ""
model = ""


async defwebsocket_handler():
"""Connect to WebSocket and handle audio streaming + transcription."""
    global transcription_text, is_running

    async with websockets.connect(ws_url) as ws:
        # Wait for session.created
        await ws.recv()

        # Validate model
        await ws.send(json.dumps({"type": "session.update", "model": model}))

        # Signal ready
        await ws.send(json.dumps({"type": "input_audio_buffer.commit"}))

        async defsend_audio():
            while is_running:
                try:
                    chunk = await asyncio.get_event_loop().run_in_executor(
                        None, lambda: audio_queue.get(timeout=0.1)
                    )
                    await ws.send(
                        json.dumps(
                            {"type": "input_audio_buffer.append", "audio": chunk}
                        )
                    )
                except queue.Empty:
                    continue

        async defreceive_transcription():
            global transcription_text
            async for message in ws:
                data = json.loads(message)
                if data.get("type") == "transcription.delta":
                    transcription_text += data["delta"]

        await asyncio.gather(send_audio(), receive_transcription())


defstart_websocket():
"""Start WebSocket connection in background thread."""
    global is_running
    is_running = True
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.run_until_complete(websocket_handler())
    except Exception as e:
        print(f"WebSocket error: {e}")


defstart_recording():
"""Start the transcription service."""
    global transcription_text
    transcription_text = ""
    thread = threading.Thread(target=start_websocket, daemon=True)
    thread.start()
    return gr.update(interactive=False), gr.update(interactive=True), ""


defstop_recording():
"""Stop the transcription service."""
    global is_running
    is_running = False
    return gr.update(interactive=True), gr.update(interactive=False), transcription_text


defprocess_audio(audio):
"""Process incoming audio and queue for streaming."""
    global transcription_text

    if audio is None or not is_running:
        return transcription_text

    sample_rate, audio_data = audio

    # Convert to mono if stereo
    if len(audio_data.shape) > 1:
        audio_data = audio_data.mean(axis=1)

    # Normalize to float
    if audio_data.dtype == np.int16:
        audio_float = audio_data.astype(np.float32) / 32767.0
    else:
        audio_float = audio_data.astype(np.float32)

    # Resample to 16kHz if needed
    if sample_rate != SAMPLE_RATE:
        num_samples = int(len(audio_float) * SAMPLE_RATE / sample_rate)
        audio_float = np.interp(
            np.linspace(0, len(audio_float) - 1, num_samples),
            np.arange(len(audio_float)),
            audio_float,
        )

    # Convert to PCM16 and base64 encode
    pcm16 = (audio_float * 32767).astype(np.int16)
    b64_chunk = base64.b64encode(pcm16.tobytes()).decode("utf-8")
    audio_queue.put(b64_chunk)

    return transcription_text


# Gradio interface
with gr.Blocks(title="Real-time Speech Transcription") as demo:
    gr.Markdown("# Real-time Speech Transcription")
    gr.Markdown("Click **Start** and speak into your microphone.")

    with gr.Row():
        start_btn = gr.Button("Start", variant="primary")
        stop_btn = gr.Button("Stop", variant="stop", interactive=False)

    audio_input = gr.Audio(sources=["microphone"], streaming=True, type="numpy")
    transcription_output = gr.Textbox(label="Transcription", lines=5)

    start_btn.click(
        start_recording, outputs=[start_btn, stop_btn, transcription_output]
    )
    stop_btn.click(stop_recording, outputs=[start_btn, stop_btn, transcription_output])
    audio_input.stream(
        process_audio, inputs=[audio_input], outputs=[transcription_output]
    )

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Realtime WebSocket Transcription with Gradio"
    )
    parser.add_argument(
        "--model",
        type=str,
        default="mistralai/Voxtral-Mini-4B-Realtime-2602",
        help="Model that is served and should be pinged.",
    )
    parser.add_argument(
        "--host", type=str, default="localhost", help="vLLM server host"
    )
    parser.add_argument("--port", type=int, default=8000, help="vLLM server port")
    parser.add_argument(
        "--share", action="store_true", help="Create public Gradio link"
    )
    args = parser.parse_args()

    ws_url = f"ws://{args.host}:{args.port}/v1/realtime"
    model = args.model
    demo.launch(share=args.share)
```
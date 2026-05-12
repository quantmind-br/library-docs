---
title: 'GLM-4.7-Flash: How To Run Locally'
url: https://unsloth.ai/docs/models/glm-4.7-flash.md
source: llms
fetched_at: 2026-04-27T18:13:45.217744325-03:00
rendered_js: false
word_count: 1917
summary: This document provides a comprehensive guide on how to run Z.ai's GLM-4.7-Flash model locally, detailing optimal usage parameters, memory requirements, and step-by-step tutorials for deployment via Unsloth Studio and llama.cpp.
tags:
    - glm-4-7-flash
    - local-deployment
    - llm-guide
    - unsloth
    - llama-cpp
    - inference
category: tutorial
optimized: true
optimized_at: 2026-04-27T21:30:00Z
---

# GLM-4.7-Flash: How To Run Locally

GLM-4.7-Flash is Z.ai's 30B MoE reasoning model (~3.6B active params, 200K context). Best-in-class for coding, agentic workflows, and chat. Leads SWE-Bench, GPQA, and reasoning/chat benchmarks.

- **RAM requirement:** 24GB VRAM/RAM/unified memory (32GB for full precision)
- **GGUF:** [unsloth/GLM-4.7-Flash-GGUF](https://huggingface.co/unsloth/GLM-4.7-Flash-GGUF)
- Fine-tuning supported via Unsloth (requires `transformers v5`, ~60GB VRAM for 16-bit LoRA)

> [!tip]
> **Jan 21 update:** `llama.cpp` fixed a bug specifying wrong `scoring_func`: `"softmax"` (should be `"sigmoid"`). This caused looping and poor outputs. Re-download the GGUF for much better outputs.
>
> **Jan 22:** Faster inference — FA fix for CUDA is now merged.

## Usage Guide

> [!tip]
> For best performance, ensure total available memory (VRAM + system RAM) exceeds the quantized model file size. If not, llama.cpp can still run via SSD/HDD offloading but inference will be slower.

Z.ai recommended sampling parameters:

| Use Case | `temperature` | `top_p` | Repeat Penalty |
|----------|--------------|---------|----------------|
| Default (most tasks) | 1.0 | 0.95 | disabled / 1.0 |
| Terminal Bench, SWE Bench | 0.7 | 1.0 | disabled / 1.0 |

- General use-case: `--temp 1.0 --top-p 0.95`
- Tool-calling: `--temp 0.7 --top-p 1.0`
- If using llama.cpp, set `--min-p 0.01` (llama.cpp default is 0.05)
- **Maximum context window:** `202,752`

> [!warning]
> Do NOT run this GGUF with Ollama due to chat template compatibility issues. Works well on llama.cpp, LM Studio, Jan.
>
> **Disable repeat penalty** or set `--repeat-penalty 1.0`

## Run GLM-4.7-Flash

Some GGUFs end up similar in size because the model architecture (like [[013-models-gpt-oss-how-to-run-and-fine-tune|gpt-oss]]) has dimensions not divisible by 128, so parts can't be quantized to lower bits. This guide uses 4-bit (~18GB RAM/unified memory). Recommend at least 4-bit precision.

### Unsloth Studio

[[097-new-studio|Unsloth Studio]] is an open-source web UI for local AI on macOS, Windows, and Linux. Features: search/download/run GGUFs and safetensors, self-healing tool calling + web search, code execution (Python/Bash), automatic inference parameter tuning, llama.cpp CPU+GPU inference, train LLMs 2x faster with 70% less VRAM.

**1. Install Unsloth**

```bash
# MacOS, Linux, WSL:
curl -fsSL https://unsloth.ai/install.sh | sh
# Windows PowerShell:
irm https://unsloth.ai/install.ps1 | iex
```

> [!tip]
> Installation takes ~1-2 mins.

**2. Launch Unsloth**

```bash
unsloth studio -H 0.0.0.0 -p 8888
```

Then open `http://localhost:8888` in your browser.

**3. Search and download GLM-4.7-Flash**

On first launch, create a password and sign in. You can skip the onboarding wizard. Go to the [[099-new-studio-chat|Studio Chat]] tab, search for **GLM-4.7-Flash**, and download your desired quant.

**4. Run GLM-4.7-Flash**

Inference parameters are auto-set but can be changed manually. Edit context length, chat template, and other settings. See the [[099-new-studio-chat|Unsloth Studio inference guide]].

### llama.cpp (GGUF)

**1. Build llama.cpp**

```bash
apt-get update
apt-get install pciutils build-essential cmake curl libcurl4-openssl-dev -y
git clone https://github.com/ggml-org/llama.cpp
cmake llama.cpp -B llama.cpp/build \
    -DBUILD_SHARED_LIBS=OFF -DGGML_CUDA=ON
cmake --build llama.cpp/build --config Release -j --clean-first --target llama-cli llama-mtmd-cli llama-server llama-gguf-split
cp llama.cpp/build/bin/llama-* llama.cpp
```

Use `-DGGML_CUDA=OFF` for CPU-only or Apple Mac/Metal (Metal is on by default).

**2. Run via HuggingFace pull**

General instruction use-case:

```bash
./llama.cpp/llama-cli \
    -hf unsloth/GLM-4.7-Flash-GGUF:UD-Q4_K_XL \
    --ctx-size 16384 \
    --temp 1.0 --top-p 0.95 --min-p 0.01
```

Tool-calling use-case:

```bash
./llama.cpp/llama-cli \
    -hf unsloth/GLM-4.7-Flash-GGUF:UD-Q4_K_XL \
    --ctx-size 16384 \
    --temp 0.7 --top-p 1.0 --min-p 0.01
```

**3. Download manually**

```bash
pip install -U huggingface_hub
hf download unsloth/GLM-4.7-Flash-GGUF \
    --local-dir unsloth/GLM-4.7-Flash-GGUF \
    --include "*UD-Q2_K_XL*"
```

If downloads get stuck, see [[124-basics-troubleshooting-and-faqs-hugging-face-hub-xet-debugging|HF XET debugging]].

**4. Run local file**

```bash
./llama.cpp/llama-cli \
    --model unsloth/GLM-4.7-Flash-GGUF/GLM-4.7-Flash-UD-Q4_K_XL.gguf \
    --ctx-size 16384 \
    --seed 3407 \
    --temp 1.0 \
    --top-p 0.95 \
    --min-p 0.01
```

Adjust context window up to `202752` as RAM/VRAM allows.

## Reducing Repetition and Looping

> [!success]
> **Jan 21 fix:** llama.cpp fixed wrong `"scoring_func": "softmax"` (should be `"sigmoid"`). Re-download the GGUF. We added `"scoring_func": "sigmoid"` to `config.json` — [see commit](https://huggingface.co/unsloth/GLM-4.7-Flash/commit/3fd53b491e04f707f307aef2f70f8a7520511e6d).

With the fix, use Z.ai's recommended parameters:
- General: `--temp 1.0 --top-p 0.95`
- Tool-calling: `--temp 0.7 --top-p 1.0`
- llama.cpp: set `--min-p 0.01`
- **Disable repeat penalty** or set `--repeat-penalty 1.0`

> [!warning]
> Do NOT run this GGUF with Ollama due to chat template compatibility issues.

## Flappy Bird Example with UD-Q4_K_XL

Long conversation via: `./llama.cpp/llama-cli --model unsloth/GLM-4.7-Flash-GGUF/GLM-4.7-Flash-UD-Q4_K_XL.gguf --fit on --temp 1.0 --top-p 0.95 --min-p 0.01`

Prompts used: Hi / What is 2+2 / Create a Python Flappy Bird game / Create a totally different game in Rust / Find bugs in both / Make the 1st game but in a standalone HTML file / Find bugs and show the fixed game

<details>

<summary>Flappy Bird Game in HTML (Expandable)</summary>

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Flappy Bird Fixed</title>
    <style>
        body {
            margin: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #222;
            font-family: 'Arial', sans-serif;
            overflow: hidden;
            user-select: none;
            -webkit-user-select: none;
            touch-action: none; /* Prevents zoom on mobile */
        }

        #game-container {
            position: relative;
            box-shadow: 0 0 20px rgba(0,0,0,0.5);
        }

        canvas {
            background-color: #87CEEB;
            display: block;
            border-radius: 4px;
        }

        /* UI Overlays */
        #ui-layer {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
        }

        #score-display {
            position: absolute;
            top: 40px;
            left: 50%;
            transform: translateX(-50%);
            font-size: 48px;
            font-weight: bold;
            color: white;
            text-shadow: 3px 3px 0 #000;
            z-index: 10;
            font-family: 'Courier New', Courier, monospace;
        }

        #start-screen, #game-over-screen {
            background: rgba(0, 0, 0, 0.7);
            width: 100%;
            height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            color: white;
            pointer-events: auto; /* Allow clicks */
            cursor: pointer;
        }

        h1 { margin: 0 0 10px 0; font-size: 60px; text-shadow: 4px 4px 0 #000; line-height: 1; }
        p { font-size: 22px; margin: 10px 0; color: #ddd; }
        
        .btn {
            background: linear-gradient(to bottom, #ffeb3b, #fbc02d);
            border: 3px solid #fff;
            color: #333;
            padding: 15px 40px;
            font-size: 28px;
            font-weight: bold;
            cursor: pointer;
            border-radius: 8px;
            box-shadow: 0 6px 0 #c49000, 0 10px 10px rgba(0,0,0,0.3);
            text-transform: uppercase;
            transition: all 0.1s;
            margin-top: 10px;
        }

        .btn:active {
            transform: translateY(4px);
            box-shadow: 0 2px 0 #c49000, 0 4px 4px rgba(0,0,0,0.3);
        }

        .score-board {
            background: #ded895;
            border: 2px solid #543847;
            padding: 20px 40px;
            border-radius: 10px;
            box-shadow: 4px 4px 0 #543847;
            margin-bottom: 30px;
            display: none;
            border: 4px solid #543847;
        }
        
        .score-board h2 { margin: 0 0 5px 0; color: #e86101; font-size: 40px; }
        .score-board span { font-size: 20px; color: #543847; display: block; text-align: center; }

    </style>
</head>
<body>

    <div id="game-container">
        <canvas id="gameCanvas" width="400" height="600"></canvas>
        
        <div id="score-display">0</div>

        <div id="ui-layer">
            <div id="start-screen">
                <h1>FLAPPY<br>BIRD</h1>
                <p>Tap or Press Space to Start</p>
                <button class="btn" style="display:none;" id="touch-instruction">Click to Start</button>
            </div>

            <div id="game-over-screen">
                <h1>GAME OVER</h1>
                <div class="score-board" id="score-board">
                    <h2>Score: <span id="final-score">0</span></h2>
                </div>
                <button class="btn" id="restart-btn">Try Again</button>
            </div>
        </div>
    </div>

<script>
    const canvas = document.getElementById('gameCanvas');
    const ctx = canvas.getContext('2d');

    // --- Constants ---
    const GRAVITY = 0.35; // Slightly harder gravity for better feel
    const JUMP_STRENGTH = -6.5;
    const PIPE_GAP = 180;
    const PIPE_WIDTH = 60;
    const PIPE_SPEED = 2.5;
    const PIPE_SPAWN_RATE = 100;

    // --- State ---
    let frames = 0;
    let score = 0;
    let isGameOver = false;
    let isPlaying = false;
    let gameLoopId;

    const ui = {
        startScreen: document.getElementById('start-screen'),
        gameOverScreen: document.getElementById('game-over-screen'),
        scoreDisplay: document.getElementById('score-display'),
        scoreBoard: document.getElementById('score-board'),
        finalScore: document.getElementById('final-score'),
        restartBtn: document.getElementById('restart-btn')
    };

    const bird = {
        x: 80,
        y: 150,
        radius: 12, // Fixed radius
        velocity: 0,
        
        draw: function() {
            // Rotate bird based on velocity for visual flair
            let angle = Math.min(Math.PI / 4, Math.max(-Math.PI / 4, (this.velocity * 0.1)));
            
            ctx.save();
            ctx.translate(this.x, this.y);
            ctx.rotate(angle);
            
            // Draw Body
            ctx.fillStyle = '#FFD700';
            ctx.beginPath();
            ctx.arc(0, 0, this.radius, 0, Math.PI * 2);
            ctx.fill();
            
            // Eye
            ctx.fillStyle = 'white';
            ctx.beginPath();
            ctx.arc(4, -4, 4, 0, Math.PI * 2);
            ctx.fill();
            ctx.fillStyle = 'black';
            ctx.beginPath();
            ctx.arc(6, -4, 2, 0, Math.PI * 2);
            ctx.fill();
            
            // Wing
            ctx.fillStyle = '#FFA500';
            ctx.beginPath();
            ctx.arc(-4, 4, 5, 0, Math.PI * 2);
            ctx.fill();

            ctx.restore();
        },

        update: function() {
            this.velocity += GRAVITY;
            this.y += this.velocity;
        },

        jump: function() {
            this.velocity = JUMP_STRENGTH;
        },

        reset: function() {
            this.y = 150;
            this.velocity = 0;
        }
    };

    let pipes = [];

    function createPipe() {
        const minHeight = 50;
        const maxPos = canvas.height - PIPE_GAP - minHeight;
        const topHeight = Math.floor(Math.random() * (maxPos - minHeight + 1)) + minHeight;
        
        pipes.push({
            x: canvas.width,
            topHeight: topHeight,
            bottomY: topHeight + PIPE_GAP,
            width: PIPE_WIDTH,
            passed: false
        });
    }

    function drawPipes() {
        ctx.fillStyle = '#2ecc71';
        ctx.strokeStyle = '#27ae60';
        ctx.lineWidth = 2;
        
        pipes.forEach(pipe => {
            // Top Pipe
            ctx.fillRect(pipe.x, 0, pipe.width, pipe.topHeight);
            ctx.strokeRect(pipe.x, 0, pipe.width, pipe.topHeight);
            
            // Bottom Pipe
            ctx.fillRect(pipe.x, pipe.bottomY, pipe.width, canvas.height - pipe.bottomY);
            ctx.strokeRect(pipe.x, pipe.bottomY, pipe.width, canvas.height - pipe.bottomY);

            // Cap
            const capH = 20;
            ctx.fillStyle = '#27ae60'; 
            ctx.fillRect(pipe.x - 2, pipe.topHeight - capH, pipe.width + 4, capH);
            ctx.fillRect(pipe.x - 2, pipe.bottomY, pipe.width + 4, capH);
        });
    }

    function updatePipes() {
        if (frames % PIPE_SPAWN_RATE === 0) createPipe();

        for (let i = 0; i < pipes.length; i++) {
            let p = pipes[i];
            p.x -= PIPE_SPEED;

            // --- FIXED COLLISION DETECTION ---
            // Treat bird as a circle of radius 'bird.radius'
            // Pipe is a rect: x, x+w, y_top, y_bottom
            let birdLeft = bird.x - bird.radius;
            let birdRight = bird.x + bird.radius;
            let birdTop = bird.y - bird.radius;
            let birdBottom = bird.y + bird.radius;

            // Horizontal Overlap
            if (birdRight > p.x && birdLeft < p.x + p.width) {
                // Vertical Overlap (Hit Top Pipe OR Hit Bottom Pipe)
                if (birdTop < p.topHeight || birdBottom > p.bottomY) {
                    gameOver();
                }
            }

            // --- FIXED SCORING ---
            // If pipe is off screen to the left, and hasn't been scored
            if (p.x + p.width < 0 && !p.passed) {
                score++;
                p.passed = true;
                ui.scoreDisplay.innerText = score;
            }

            if (p.x < -60) {
                pipes.shift();
                i--;
            }
        }
    }

    function checkCollisions() {
        // Floor
        if (bird.y + bird.radius >= canvas.height) {
            gameOver();
        }
        // Ceiling
        if (bird.y - bird.radius <= 0) {
            bird.y = bird.radius;
            bird.velocity = 0;
        }
    }

    function drawBackground() {
        // Clear
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        // Floor
        ctx.fillStyle = '#654321';
        ctx.fillRect(0, canvas.height - 10, canvas.width, 10);
        
        // Clouds
        ctx.fillStyle = "rgba(255, 255, 255, 0.6)";
        for(let i=0; i<4; i++) {
            let x = (frames * 0.5 + i * 150) % (canvas.width + 100) - 50;
            let y = (i * 40) + 20;
            let scale = 1 + (Math.sin(frames * 0.02 + i) * 0.1);
            let size = 30 * scale;
            ctx.beginPath();
            ctx.arc(x, y, size, 0, Math.PI * 2);
            ctx.arc(x + 20*scale, y - 10*scale, size * 1.2, 0, Math.PI * 2);
            ctx.arc(x + 40*scale, y, size, 0, Math.PI * 2);
            ctx.fill();
        }
    }

    function update() {
        if (!isPlaying) return;
        bird.update();
        updatePipes();
        checkCollisions();
        frames++;
    }

    function draw() {
        drawBackground();
        drawPipes();
        bird.draw();
    }

    function loop() {
        update();
        draw();
        if (isPlaying || !isGameOver) {
            gameLoopId = requestAnimationFrame(loop);
        }
    }

    function startGame() {
        isPlaying = true;
        isGameOver = false;
        
        // UI
        ui.startScreen.style.display = 'none';
        ui.gameOverScreen.style.display = 'none';
        ui.scoreBoard.style.display = 'none';
        
        // Logic
        bird.reset();
        pipes = [];
        score = 0;
        frames = 0;
        ui.scoreDisplay.innerText = '0';
        
        loop();
    }

    function gameOver() {
        isPlaying = false;
        isGameOver = true;
        cancelAnimationFrame(gameLoopId);
        
        ui.finalScore.innerText = score;
        ui.gameOverScreen.style.display = 'flex';
        ui.scoreBoard.style.display = 'block';
    }

    // --- Input Handling ---

    function handleInput(e) {
        if (e.type === 'keydown' && e.code === 'Space') e.preventDefault();

        if (isPlaying) {
            bird.jump();
        } else if (!isGameOver) {
            // Click on start screen (or any click if game hasn't started)
            startGame();
        }
    }

    // Keyboard
    window.addEventListener('keydown', (e) => {
        if (e.code === 'Space') handleInput(e);
    });

    // Mouse / Touch
    window.addEventListener('mousedown', handleInput);
    window.addEventListener('touchstart', (e) => {
        // Prevent zoom/scroll
        // e.preventDefault(); 
        handleInput(e);
    }, {passive: false});

    // UI Interactions
    ui.restartBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        startGame();
    });
    
    // Allow clicking the Game Over overlay to restart
    ui.gameOverScreen.addEventListener('mousedown', (e) => {
        if(e.target === ui.gameOverScreen) startGame();
    });
    ui.gameOverScreen.addEventListener('touchstart', (e) => {
        if(e.target === ui.gameOverScreen) {
            e.preventDefault();
            startGame();
        }
    });

    // Initial Draw
    drawBackground();
    bird.reset();
    bird.draw();

</script>
</body>
</html>
```

</details>

## Fine-tuning GLM-4.7-Flash

Requires `transformers v5`. 30B model does not fit on free Colab GPU. 16-bit LoRA fine-tuning uses ~60GB VRAM.

- [GLM-4.7-Flash SFT LoRA notebook](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/GLM_Flash_A100\(80GB\).ipynb)

> [!warning]
> May OOM on A100 40GB. Use H100/A100 80GB for smoother runs.

MoE router layer is disabled by default during fine-tuning. To maintain reasoning capabilities: use a mix of direct answers and chain-of-thought examples — at least **75% reasoning** and **25% non-reasoning** in your dataset.

## Llama-server serving & deployment

Deploy via `llama-server`:

```bash
./llama.cpp/llama-server \
    --model unsloth/GLM-4.7-Flash-GGUF/GLM-4.7-Flash-UD-Q4_K_XL.gguf \
    --alias "unsloth/GLM-4.7-Flash" \
    --seed 3407 \
    --temp 1.0 \
    --top-p 0.95 \
    --min-p 0.01 \
    --ctx-size 16384 \
    --port 8001
```

Call via OpenAI API (`pip install openai`):

```python
from openai import OpenAI
import json
openai_client = OpenAI(
    base_url = "http://127.0.0.1:8001/v1",
    api_key = "sk-no-key-required",
)
completion = openai_client.chat.completions.create(
    model = "unsloth/GLM-4.7-Flash",
    messages = [{"role": "user", "content": "What is 2+2?"},],
)
print(completion.choices[0].message.content)
```

## GLM-4.7-Flash in vLLM

Use the [FP8 Dynamic quant](https://huggingface.co/unsloth/GLM-4.7-Flash-FP8-Dynamic) for premium fast inference. Install vLLM from nightly:

```bash
uv pip install --upgrade --force-reinstall vllm --torch-backend=auto --extra-index-url https://wheels.vllm.ai/nightly/cu130
uv pip install --upgrade --force-reinstall git+https://github.com/huggingface/transformers.git
uv pip install --force-reinstall numba
```

Serve the model (FP8 reduces KV cache memory 50%):

```bash
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:False
CUDA_VISIBLE_DEVICES='0,1,2,3' vllm serve unsloth/GLM-4.7-Flash-FP8-Dynamic \
    --served-model-name unsloth/GLM-4.7-Flash \
    --tensor-parallel-size 4 \
    --tool-call-parser glm47 \
    --reasoning-parser glm45 \
    --enable-auto-tool-choice \
    --dtype bfloat16 \
    --seed 3407 \
    --max-model-len 200000 \
    --gpu-memory-utilization 0.95 \
    --max_num_batched_tokens 16384 \
    --port 8001 \
    --kv-cache-dtype fp8
```

For 1 GPU: use `CUDA_VISIBLE_DEVICES='0'` and set `--tensor-parallel-size 1` or remove. To disable FP8, remove `--quantization fp8 --kv-cache-dtype fp8`.

Then call via OpenAI API:

```python
from openai import AsyncOpenAI, OpenAI
openai_api_key = "EMPTY"
openai_api_base = "http://localhost:8001/v1"
client = OpenAI( # or AsyncOpenAI
    api_key=openai_api_key,
    base_url=openai_api_base,
)
```

### vLLM Speculative Decoding

Using the MTP (multi token prediction) module drops throughput from 13,000 tok/s to 1,300 tok/s on 1xB200 (10x slower). On Hopper it should be fine.

```bash
    --speculative-config.method mtp \
    --speculative-config.num_speculative_tokens 1
```

## Tool Calling with GLM-4.7-Flash

See [[095-basics-tool-calling-guide-for-local-llms|Tool Calling Guide for Local LLMs]] for details. After launching GLM-4.7-Flash via `llama-server` (above), define tools and run inference:

```python
import json, subprocess, random
from typing import Any
def add_number(a: float | str, b: float | str) -> float:
    return float(a) + float(b)
def multiply_number(a: float | str, b: float | str) -> float:
    return float(a) * float(b)
def substract_number(a: float | str, b: float | str) -> float:
    return float(a) - float(b)
def write_a_story() -> str:
    return random.choice([
        "A long time ago in a galaxy far far away...",
        "There were 2 friends who loved sloths and code...",
        "The world was ending because every sloth evolved to have superhuman intelligence...",
        "Unbeknownst to one friend, the other accidentally coded a program to evolve sloths...",
    ])
def terminal(command: str) -> str:
    if "rm" in command or "sudo" in command or "dd" in command or "chmod" in command:
        msg = "Cannot execute 'rm, sudo, dd, chmod' commands since they are dangerous"
        print(msg); return msg
    print(f"Executing terminal command `{command}`")
    try:
        return str(subprocess.run(command, capture_output = True, text = True, shell = True, check = True).stdout)
    except subprocess.CalledProcessError as e:
        return f"Command failed: {e.stderr}"
def python(code: str) -> str:
    data = {}
    exec(code, data)
    del data["__builtins__"]
    return str(data)
MAP_FN = {
    "add_number": add_number,
    "multiply_number": multiply_number,
    "substract_number": substract_number,
    "write_a_story": write_a_story,
    "terminal": terminal,
    "python": python,
}
tools = [
    {
        "type": "function",
        "function": {
            "name": "add_number",
            "description": "Add two numbers.",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {
                        "type": "string",
                        "description": "The first number.",
                    },
                    "b": {
                        "type": "string",
                        "description": "The second number.",
                    },
                },
                "required": ["a", "b"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "multiply_number",
            "description": "Multiply two numbers.",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {
                        "type": "string",
                        "description": "The first number.",
                    },
                    "b": {
                        "type": "string",
                        "description": "The second number.",
                    },
                },
                "required": ["a", "b"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "substract_number",
            "description": "Substract two numbers.",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {
                        "type": "string",
                        "description": "The first number.",
                    },
                    "b": {
                        "type": "string",
                        "description": "The second number.",
                    },
                },
                "required": ["a", "b"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "write_a_story",
            "description": "Writes a random story.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": [],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "terminal",
            "description": "Perform operations from the terminal.",
            "parameters": {
                "type": "object",
                "properties": {
                    "command": {
                        "type": "string",
                        "description": "The command you wish to launch, e.g `ls`, `rm`, ...",
                    },
                },
                "required": ["command"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "python",
            "description": "Call a Python interpreter with some Python code that will be ran.",
            "parameters": {
                "type": "object",
                "properties": {
                    "code": {
                        "type": "string",
                        "description": "The Python code to run",
                    },
                },
                "required": ["code"],
            },
        },
    },
]
```

Inference loop (parses tool calls automatically, calls OpenAI endpoint):

```python
from openai import OpenAI
def unsloth_inference(
    messages,
    temperature = 0.7,
    top_p = 1.0,
    top_k = -1,
    repetition_penalty = 0.0,
):
    messages = messages.copy()
    openai_client = OpenAI(
        base_url = "http://127.0.0.1:8001/v1",
        api_key = "sk-no-key-required",
    )
    model_name = next(iter(openai_client.models.list())).id
    print(f"Using model = {model_name}")
    has_tool_calls = True
    original_messages_len = len(messages)
    while has_tool_calls:
        print(f"Current messages = {messages}")
        response = openai_client.chat.completions.create(
            model = model_name,
            messages = messages,
            temperature = temperature,
            top_p = top_p,
            tools = tools if tools else None,
            tool_choice = "auto" if tools else None,
            extra_body = {"top_k": top_k, "min_p": min_p, "dry_multiplier" :repetition_penalty,}
        )
        tool_calls = response.choices[0].message.tool_calls or []
        content = response.choices[0].message.content or ""
        tool_calls_dict = [tc.to_dict() for tc in tool_calls] if tool_calls else tool_calls
        messages.append({"role": "assistant", "tool_calls": tool_calls_dict, "content": content,})
        for tool_call in tool_calls:
            fx, args, _id = tool_call.function.name, tool_call.function.arguments, tool_call.id
            out = MAP_FN[fx](**json.loads(args))
            messages.append({"role": "tool", "tool_call_id": _id, "name": fx, "content": str(out),})
        else:
            has_tool_calls = False
    return messages
```

Tool call examples:

```python
# Math
messages = [{
    "role": "user",
    "content": [{"type": "text", "text": "What is today's date plus 3 days?"}],
}]
unsloth_inference(messages, temperature = 1.0, top_p = 0.95, top_k = -1, min_p = 0.01)

# Python code execution
messages = [{
    "role": "user",
    "content": [{"type": "text", "text": "Create a Fibonacci function in Python and find fib(20)."}],
}]
unsloth_inference(messages, temperature = 1.0, top_p = 0.95, top_k = -1, min_p = 0.01)
```

## Benchmarks

GLM-4.7-Flash is the best performing 30B model across all benchmarks except AIME 25.

| Benchmark | GLM-4.7-Flash | Qwen3-30B-A3B-Thinking-2507 | GPT-OSS-20B |
|-----------|---------------|---------------------------|-------------|
| AIME 25 | 91.6 | 85.0 | 91.7 |
| GPQA | 75.2 | 73.4 | 71.5 |
| LCB v6 | 64.0 | 66.0 | 61.0 |
| HLE | 14.4 | 9.8 | 10.9 |
| SWE-bench Verified | 59.2 | 22.0 | 34.0 |
| τ²-Bench | 79.5 | 49.0 | 47.7 |
| BrowseComp | 42.8 | 2.29 | 28.3 |

---

# Agent Instructions: Querying This Documentation

If you need additional information not on this page, query the documentation dynamically:

```
GET https://unsloth.ai/docs/models/glm-4.7-flash.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language. The response contains a direct answer with relevant excerpts and sources.

#glm-4-7-flash #local-inference #gguf #unsloth-studio #llama-cpp

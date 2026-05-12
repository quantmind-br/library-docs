---
title: Hardware peripherals design
authors:
  - ZeroClaw Team
tags:
  - ai-agent
  - embedded-systems
  - rust-lang
  - hardware-interfacing
  - rag
  - microcontroller
  - edge-computing
  - peripheral-design
category: concept
optimized: true
optimized_at: 2026-05-05T10:00:00Z
word_count: 1594
---
# Thiết kế Hardware Peripherals — ZeroClaw

> ZeroClaw enables microcontrollers and embedded systems to interpret natural language commands, synthesize hardware-specific code, and perform real-time peripheral control.

## Tóm tắt nhanh

ZeroClaw transforms natural language commands into hardware control actions through:

- **Natural language understanding** via LLM integration
- **Hardware-aware code synthesis** using RAG pipelines with datasheets and register maps
- **Real-time peripheral execution** through GPIO, I2C, SPI, and memory operations
- **Two operational modes**: Edge-Native (on-device) and Host-Mediated (server-based)

## 1. Tầm nhìn cốt lõi

ZeroClaw serves as a **hardware-aware AI agent** that:

- Receives natural language commands (e.g., "Turn on LED on pin 13") via messaging channels (WhatsApp, Telegram)
- Retrieves accurate hardware documentation (datasheets, register maps)
- Synthesizes Rust code using LLMs (Gemini or open-source models)
- Executes logic to control peripherals (GPIO, I2C, SPI)
- Stores optimized code for reuse

> **Metaphor**: ZeroClaw = the brain that understands hardware. Peripherals = the limbs it controls.

## 2. Hai chế độ vận hành chính

### Chế độ 1: Edge-Native (Chạy trực tiếp trên thiết bị)

**Mục tiêu**: Boards with WiFi (ESP32, Raspberry Pi).

ZeroClaw runs **directly on the device**. The board starts a gRPC/nanoRPC server and communicates with peripherals locally.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  ZeroClaw on ESP32 / Raspberry Pi (Edge-Native)                             │
│                                                                             │
│  ┌─────────────┐    ┌──────────────┐    ┌─────────────────────────────────┐ │
│  │ Channels    │───►│ Agent Loop   │───►│ RAG: datasheets, register maps  │ │
│  │ WhatsApp    │    │ (LLM calls)  │    │ → LLM context                    │ │
│  │ Telegram    │    └──────┬───────┘    └─────────────────────────────────┘ │
│  └─────────────┘           │                                                 │
│                            ▼                                                 │
│  ┌─────────────────────────────────────────────────────────────────────────┐│
│  │ Code synthesis → Wasm / dynamic exec → GPIO / I2C / SPI → persist       ││
│  └─────────────────────────────────────────────────────────────────────────┘│
│                                                                             │
│  gRPC/nanoRPC server ◄──► Peripherals (GPIO, I2C, SPI, sensors, actuators)  │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Luồng xử lý**:

1. User sends WhatsApp: "Turn on LED on pin 13"
2. ZeroClaw retrieves board-specific documentation (e.g., ESP32 GPIO map)
3. LLM synthesizes Rust code
4. Code executes in sandbox (Wasm or dynamic linking)
5. GPIO is toggled; result returned to user
6. Optimized code stored for future reuse

> **All processing happens on-device. No central server required.**

### Chế độ 2: Host-Mediated (Phát triển/Gỡ lỗi)

**Mục tiêu**: Hardware connected via USB/J-Link/Aardvark to a host machine (macOS, Linux).

ZeroClaw runs on the **host machine** and maintains hardware connections to target devices. Used for development, introspection, and firmware flashing.

```
┌─────────────────────┐                    ┌──────────────────────────────────┐
│  ZeroClaw on Mac    │   USB / J-Link /   │  STM32 Nucleo-F401RE              │
│                     │   Aardvark         │  (or other MCU)                    │
│  - Channels         │ ◄────────────────► │  - Memory map                     │
│  - LLM              │                    │  - Peripherals (GPIO, ADC, I2C)    │
│  - Hardware probe   │   VID/PID          │  - Flash / RAM                     │
│  - Flash / debug    │   discovery        │                                    │
└─────────────────────┘                    └──────────────────────────────────┘
```

**Luồng xử lý**:

1. User sends Telegram: "What are the readable memory addresses on this USB device?"
2. ZeroClaw identifies connected hardware (VID/PID, architecture)
3. Performs memory mapping; suggests available address ranges
4. Returns results to user

**Or**:

1. User: "Flash this firmware to the Nucleo"
2. ZeroClaw flashes firmware via OpenOCD or probe-rs
3. Confirms success

**Or (auto-detection)**:

1. ZeroClaw detects: "STM32 Nucleo on /dev/ttyACM0, ARM Cortex-M4"
2. Suggests: "I can read/write GPIO, ADC, flash. What would you like to do?"

## 3. So sánh hai chế độ

| Khía cạnh | Edge-Native | Host-Mediated |
|-----------|-------------|---------------|
| ZeroClaw runs on | Device (ESP32, RPi) | Host machine (Mac, Linux) |
| Hardware connection | Local (GPIO, I2C, SPI) | USB, J-Link, Aardvark |
| LLM | On-device or cloud (Gemini) | Host machine (cloud or local) |
| Use cases | Production, standalone | Development, debugging, introspection |
| Communication channels | WhatsApp, etc. (via WiFi) | Telegram, CLI, etc. |

## 4. Legacy modes (Pre-LLM Edge)

### Chế độ A: Host + Remote Peripheral (STM32 via serial)

Host runs ZeroClaw; peripheral runs minimal firmware. Simple JSON over serial.

### Chế độ B: RPi as Host (Native GPIO)

ZeroClaw on Pi; GPIO via rppal or sysfs. No separate firmware needed.

## 5. Yêu cầu kỹ thuật

| Yêu cầu | Chi tiết kỹ thuật |
|---------|-------------------|
| **Ngôn ngữ** | Pure Rust. `no_std` for bare-metal targets (STM32, ESP32) |
| **Giao tiếp** | Lightweight gRPC or nanoRPC stack for low-latency command processing |
| **Dynamic execution** | Safely execute LLM-generated logic in real-time: Wasm runtime for isolation, or dynamic linking when supported |
| **Document retrieval** | RAG pipeline to inject datasheet excerpts, register maps, and pinouts into LLM context |
| **Hardware identification** | USB device recognition via VID/PID; architecture detection (ARM Cortex-M, RISC-V, etc.) |

### RAG Pipeline (Datasheet Retrieval)

1. **Indexing**: Datasheets, reference guides, register maps (PDF → chunks, embeddings)
2. **Retrieval**: On user query (e.g., "turn on LED"), fetch relevant chunks (e.g., GPIO section for target board)
3. **Injection**: Add to system prompt or LLM context
4. **Result**: LLM generates board-specific, accurate code

### Dynamic Execution Options

| Option | Pros | Cons |
|--------|------|------|
| **Wasm** | Sandboxed, portable, no FFI | Overhead; limited hardware access from Wasm |
| **Dynamic linking** | Native speed, full hardware access | Platform-dependent; security concerns |
| **Interpreted DSL** | Safe, inspectable | Slower; limited expressiveness |
| **Pre-compiled templates** | Fast, secure | Less flexible; needs template library |

> **Recommendation**: Start with pre-compiled templates + parameterization; advance to Wasm for user-defined logic once stable.

## 6. CLI và Cấu hình

### CLI Flags

```bash
# Edge-Native: run on device (ESP32, RPi)
zeroclaw agent --mode edge

# Host-Mediated: connect to USB/J-Link target
zeroclaw agent --peripheral nucleo-f401re:/dev/ttyACM0
zeroclaw agent --probe jlink

# Hardware introspection
zeroclaw hardware discover
zeroclaw hardware introspect /dev/ttyACM0
```

### Cấu hình (config.toml)

```toml
[peripherals]
enabled = true
mode = "host"  # "edge" | "host"
datasheet_dir = "docs/datasheets"  # RAG: board-specific docs for LLM context

[[peripherals.boards]]
board = "nucleo-f401re"
transport = "serial"
path = "/dev/ttyACM0"
baud = 115200

[[peripherals.boards]]
board = "rpi-gpio"
transport = "native"

[[peripherals.boards]]
board = "esp32"
transport = "wifi"
# Edge-Native: ZeroClaw runs on ESP32
```

## 7. Kiến trúc: Peripheral là điểm mở rộng

### Trait `Peripheral`

```rust
/// A hardware peripheral that exposes capabilities as tools.
#[async_trait]
pub trait Peripheral: Send + Sync {
    fn name(&self) -> &str;
    fn board_type(&self) -> &str;  // e.g. "nucleo-f401re", "rpi-gpio"
    async fn connect(&mut self) -> anyhow::Result<()>;
    async fn disconnect(&mut self) -> anyhow::Result<()>;
    async fn health_check(&self) -> bool;
    /// Tools this peripheral provides (gpio_read, gpio_write, sensor_read, etc.)
    fn tools(&self) -> Vec<Box<dyn Tool>>;
}
```

### Luồng xử lý

1. **Startup**: ZeroClaw loads config, reads `peripherals.boards`
2. **Connection**: For each board, create `Peripheral` impl, call `connect()`
3. **Tools**: Collect tools from all connected peripherals; merge with default tools
4. **Agent loop**: Agent can call `gpio_write`, `sensor_read`, etc. — commands forwarded to peripheral
5. **Shutdown**: Call `disconnect()` on each peripheral

### Board Support Matrix

| Board | Transport | Firmware / Driver | Tools |
|-------|-----------|-------------------|-------|
| nucleo-f401re | serial | Zephyr / Embassy | gpio_read, gpio_write, adc_read |
| rpi-gpio | native | rppal or sysfs | gpio_read, gpio_write |
| esp32 | serial/ws | ESP-IDF / Embassy | gpio, wifi, mqtt |

## 8. Giao thức giao tiếp

### gRPC / nanoRPC (Edge-Native, Host-Mediated)

For typed, low-latency RPC between ZeroClaw and peripherals:

- **nanoRPC** or **tonic** (gRPC): Protobuf-defined service
- Methods: `GpioWrite`, `GpioRead`, `I2cTransfer`, `SpiTransfer`, `MemoryRead`, `FlashWrite`, etc.
- Supports streaming, bidirectional calls, and code generation from `.proto` files

### Serial Fallback (Host-Mediated, legacy)

Simple JSON over serial for boards without gRPC support:

**Request (host → peripheral):**
```json
{"id":"1","cmd":"gpio_write","args":{"pin":13,"value":1}}
```

**Response (peripheral → host):**
```json
{"id":"1","ok":true,"result":"done"}
```

## 9. Firmware (Separate Repo/Crate)

- **zeroclaw-firmware** or **zeroclaw-peripheral** — a separate crate/workspace
- Targets: `thumbv7em-none-eabihf` (STM32), `armv7-unknown-linux-gnueabihf` (RPi), etc.
- Uses `embassy` or Zephyr for STM32
- Implements the protocol above
- User flashes to board; ZeroClaw connects and auto-discovers capabilities

## 10. Implementation Phases

### Phase 1: Skeleton ✅

- [x] Add `Peripheral` trait, config schema, CLI (`zeroclaw peripheral list/add`)
- [x] Add `--peripheral` flag for agent
- [x] Document in AGENTS.md

### Phase 2: Host-Mediated — Hardware Discovery ✅

- [x] `zeroclaw hardware discover`: list USB devices (VID/PID)
- [x] Board registry: map VID/PID → architecture, name (e.g., Nucleo-F401RE)
- [x] `zeroclaw hardware introspect <path>`: memory map, peripheral list

### Phase 3: Host-Mediated — Serial / J-Link

- [x] `SerialPeripheral` for STM32 over USB CDC
- [ ] Integrate probe-rs or OpenOCD for firmware flashing/debugging
- [x] Tools: `gpio_read`, `gpio_write` (future: memory_read, flash_write)

### Phase 4: RAG Pipeline ✅

- [x] Index datasheets (markdown/text → chunks)
- [x] Retrieve and inject into LLM context for hardware-related queries
- [x] Add board-specific prompts

> **Usage**: Add `datasheet_dir = "docs/datasheets"` under `[peripherals]` in config.toml. Place `.md` or `.txt` files named after board (e.g., `nucleo-f401re.md`, `rpi-gpio.md`). Files in `_generic/` or named `generic.md` apply to all boards. Chunks are retrieved by keyword and injected into user message context.

### Phase 5: Edge-Native — Raspberry Pi ✅

- [x] ZeroClaw on Raspberry Pi (native GPIO via rppal)
- [ ] gRPC/nanoRPC server for local peripheral access
- [ ] Code storage (persist synthesized code snippets)

### Phase 6: Edge-Native — ESP32

- [x] ESP32 via Host-Mediated (serial transport) — same JSON protocol as STM32
- [x] Firmware crate `esp32` (`firmware/esp32`) — GPIO over UART
- [x] ESP32 in hardware registry (CH340 VID/PID)
- [ ] ZeroClaw *runs directly on* ESP32 (WiFi + LLM, edge-native) — future
- [ ] Execute Wasm or template-based logic from LLM generation

> **Usage**: Flash `firmware/esp32` to ESP32, add `board = "esp32"`, `transport = "serial"`, `path = "/dev/ttyUSB0"` to config.

### Phase 7: Dynamic Execution (LLM-generated code)

- [ ] Template library: parameterized GPIO/I2C/SPI snippets
- [ ] Optional: Wasm runtime for user-defined logic (sandboxed)
- [ ] Store and reuse optimized code paths

## 11. Security Considerations

- **Serial path**: Validate `path` is in allowlist (e.g., `/dev/ttyACM*`, `/dev/ttyUSB*`); never use arbitrary paths
- **GPIO**: Restrict which pins can be accessed; avoid power/reset pins
- **Secrets**: Never store API keys on peripheral; host handles authentication

## 12. Out of Scope (Currently)

- Running full ZeroClaw *directly on* bare-metal STM32 (no WiFi, limited RAM) — use Host-Mediated instead
- Hard real-time guarantees — peripherals operate best-effort
- Arbitrary native code execution from LLM — prefer Wasm or templates

## 13. Tài liệu liên quan

- [[036-i18n-vi-adding-boards-and-tools|adding-boards-and-tools]] — How to add boards and datasheets
- [[039-i18n-vi-network-deployment|network-deployment]] — RPi deployment and networking

## 14. Tham khảo

- [Zephyr RTOS Rust support](https://docs.zephyrproject.org/latest/develop/languages/rust/index.html)
- [Embassy](https://embassy.dev/) — async embedded framework
- [rppal](https://github.com/golemparts/rppal) — Raspberry Pi GPIO in Rust
- [STM32 Nucleo-F401RE](https://www.st.com/en/evaluation-tools/nucleo-f401re.html)
- [tonic](https://github.com/hyperium/tonic) — gRPC for Rust
- [probe-rs](https://probe.rs/) — ARM debug probe, flash, memory access
- [nusb](https://github.com/nic-hartley/nusb) — USB device enumeration (VID/PID)

## 15. Tóm tắt ý tưởng gốc

> "Boards like ESP, Raspberry Pi, or any with WiFi can connect to an LLM (Gemini or open-source). ZeroClaw runs on the device, creates its own gRPC, starts it, and talks to the peripherals. User asks on WhatsApp: 'move arm X' or 'turn on LED'. ZeroClaw gets the exact docs, writes the code, executes it, stores the optimized version, runs it, and turns on the LED — all on the dev board.
>
> For STM Nucleo connected via USB/J-Link/Aardvark to a Mac: ZeroClaw from the Mac accesses the hardware, sets or flashes what's needed, and returns results. Example: 'Hey ZeroClaw, what are the readable/available addresses on this USB device?' It can figure out what device is connected where and give suggestions."

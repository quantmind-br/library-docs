---
title: 'QwQ-32B: How to Run effectively'
url: https://unsloth.ai/docs/models/tutorials/qwq-32b-how-to-run-effectively.md
source: llms
fetched_at: 2026-04-27T18:14:38.764482099-03:00
rendered_js: false
word_count: 1313
summary: This guide details how to effectively run the QwQ-32B reasoning model, addressing common issues like infinite generations and repetitions, while providing recommended settings for various environments.
tags:
    - qwq-32b
    - inference-tuning
    - llm-running
    - sampling-parameters
    - ollama-guide
    - llama-cpp
category: tutorial
optimized: true
optimized_at: 2026-04-27T21:37:00Z
---

# QwQ-32B: How to Run Effectively

Qwen's QwQ-32B is a reasoning model comparable to DeepSeek-R1 on [benchmarks](https://qwenlm.github.io/blog/qwq-32b/). Known issues: **infinite generations**, **repetitions**, token issues, and finetuning bugs.

> [!info] Unsloth bug-fixed uploads
> Our uploads work for fine-tuning, vLLM, and Transformers. For llama.cpp and engines using it as backend, follow the [[049-models-tutorials-qwq-32b-how-to-run-effectively|#tutorial-how-to-run-qwq-32b-in-llamacpp]] section to fix endless generations.

**Unsloth QwQ-32B uploads with bug fixes:**

| [GGUF](https://huggingface.co/unsloth/QwQ-32B-GGUF) | [Dynamic 4-bit](https://huggingface.co/unsloth/QwQ-32B-unsloth-bnb-4bit) | [BnB 4-bit](https://huggingface.co/unsloth/QwQ-32B-bnb-4bit) | [16-bit](https://huggingface.co/unsloth/QwQ-32B) |
| --------------------------------------------------- | ------------------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------ |

## Official Recommended Settings

Per [Qwen](https://huggingface.co/Qwen/QwQ-32B):

- **Temperature** — 0.6
- **Top_K** — 40 (or 20 to 40)
- **Min_P** — 0.00 (optional; 0.01 works well)
- **Top_P** — 0.95
- **Repetition Penalty** — 1.0 (disabled in llama.cpp and transformers)
- **Chat template** — `<|im_start|>user\n...\n<|im_end|>\n<|im_start|>assistant\n{}\n`

> [!warning] llama.cpp min_p default
> `llama.cpp` uses `min_p = 0.1` by default — force it to `0.0`.

## Recommended Settings for llama.cpp

Using `Repetition Penalty > 1.0` (e.g. 1.1–1.5) interferes with llama.cpp's sampling and can cause endless generations. Setting it to 1.0 (off) works but the penalty is useful to prevent infinite output.

**Critical fix**: reorder samplers so `Repetition Penalty` is applied before other samplers. Without this, you get endless generations.

```bash
--samplers "top_k;top_p;min_p;temperature;dry;typ_p;xtc"
```

Default llama.cpp ordering (problematic):

```bash
--samplers "dry;top_k;typ_p;top_p;min_p;xtc;temperature"
```

With the fix, samplers apply in order:

```bash
top_k=40
top_p=0.95
min_p=0.0
temperature=0.6
dry
typ_p
xtc
```

If issues persist, increase `--repeat-penalty` to 1.2 or 1.3.

Courtesy to [@krist486](https://x.com/krist486/status/1897885598196654180).

## Dry Repetition Penalty

Using `dry penalty = 0.8` (per [llama.cpp docs](https://github.com/ggml-org/llama.cpp/blob/master/examples/main/README.md)) **causes syntax issues especially for coding**. If needed, try `dry penalty = 0.8` with the swapped sampling ordering above.

## Tutorial: How to Run QwQ-32B in Ollama

1. Install Ollama:

```bash
apt-get update
apt-get install pciutils -y
curl -fsSL https://ollama.com/install.sh | sh
```

2. Run the model (call `ollama serve` in another terminal if it fails). Unsloth's HF upload includes all fixes and suggested parameters in `param`:

```bash
ollama run hf.co/unsloth/QwQ-32B-GGUF:Q4_K_M
```

## Tutorial: How to Run QwQ-32B in llama.cpp {#tutorial-how-to-run-qwq-32b-in-llamacpp}

1. Build llama.cpp from [GitHub](https://github.com/ggml-org/llama.cpp). Change `-DGGML_CUDA=ON` to `-DGGML_CUDA=OFF` for CPU-only. **Apple Mac / Metal**: set `-DGGML_CUDA=OFF` — Metal is on by default.

```bash
apt-get update
apt-get install pciutils build-essential cmake curl libcurl4-openssl-dev -y
git clone https://github.com/ggml-org/llama.cpp
cmake llama.cpp -B llama.cpp/build \
    -DBUILD_SHARED_LIBS=ON -DGGML_CUDA=ON -DLLAMA_CURL=ON
cmake --build llama.cpp/build --config Release -j --clean-first --target llama-quantize llama-cli llama-gguf-split
cp llama.cpp/build/bin/llama-* llama.cpp
```

2. Download the model (after `pip install huggingface_hub hf_transfer`). Choose Q4_K_M or other quants at [Unsloth QwQ-32B-GGUF](https://huggingface.co/unsloth/QwQ-32B-GGUF):

```python
# !pip install huggingface_hub hf_transfer
import os
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"
from huggingface_hub import snapshot_download
snapshot_download(
    repo_id = "unsloth/QwQ-32B-GGUF",
    local_dir = "unsloth-QwQ-32B-GGUF",
    allow_patterns = ["*Q4_K_M*"], # For Q4_K_M
)
```

3. Run Unsloth's Flappy Bird test — output saves to `Q4_K_M_yes_samplers.txt`.
4. Adjust `--threads 32` (CPU threads), `--ctx-size 16384` (context length), `--n-gpu-layers 99` (GPU offloading layers — lower if OOM, remove for CPU-only). Uses `--repeat-penalty 1.1` and `--dry-multiplier 0.5`.

```bash
./llama.cpp/llama-cli \
    --model unsloth-QwQ-32B-GGUF/QwQ-32B-Q4_K_M.gguf \
    --threads 32 \
    --ctx-size 16384 \
    --n-gpu-layers 99 \
    --seed 3407 \
    --prio 2 \
    --temp 0.6 \
    --repeat-penalty 1.1 \
    --dry-multiplier 0.5 \
    --min-p 0.01 \
    --top-k 40 \
    --top-p 0.95 \
    -no-cnv \
    --samplers "top_k;top_p;min_p;temperature;dry;typ_p;xtc" \
    --prompt "<|im_start|>user\nCreate a Flappy Bird game in Python. You must include these things:\n1. You must use pygame.\n2. The background color should be randomly chosen and is a light shade. Start with a light blue color.\n3. Pressing SPACE multiple times will accelerate the bird.\n4. The bird's shape should be randomly chosen as a square, circle or triangle. The color should be randomly chosen as a dark color.\n5. Place on the bottom some land colored as dark brown or yellow chosen randomly.\n6. Make a score shown on the top right side. Increment if you pass pipes and don't hit them.\n7. Make randomly spaced pipes with enough space. Color them randomly as dark green or light brown or a dark gray shade.\n8. When you lose, show the best score. Make the text inside the screen. Pressing q or Esc will quit the game. Restarting is pressing SPACE again.\nThe final game should be inside a markdown section in Python. Check your code for errors and fix them before the final markdown section.<|im_end|>\n<|im_start|>assistant\n{}\n"  \
        2>&1 | tee Q4_K_M_yes_samplers.txt
```

Full input prompt from the [1.58-bit blog](https://unsloth.ai/blog/deepseekr1-dynamic):

```
<|im_start|>user
Create a Flappy Bird game in Python. You must include these things:
1. You must use pygame.
2. The background color should be randomly chosen and is a light shade. Start with a light blue color.
3. Pressing SPACE multiple times will accelerate the bird.
4. The bird's shape should be randomly chosen as a square, circle or triangle. The color should be randomly chosen as a dark color.
5. Place on the bottom some land colored as dark brown or yellow chosen randomly.
6. Make a score shown on the top right side. Increment if you pass pipes and don't hit them.
7. Make randomly spaced pipes with enough space. Color them randomly as dark green or light brown or a dark gray shade.
8. When you lose, show the best score. Make the text inside the screen. Pressing q or Esc will quit the game. Restarting is pressing SPACE again.
The final game should be inside a markdown section in Python. Check your code for errors and fix them before the final markdown section.<|im_end|>
<|im_start|>assistant
{}
```

Beginning/end of the correct Python output (thinking parts removed):

```python
import pygame
import random
import sys

pygame.init()
### Continues

class Bird:
    def __init__(self):
        ### Continues

def main():
    best_score = 0
    current_score = 0
    game_over = False
    pipes = []
    first_time = True  # Track first game play

    # Initial setup
    background_color = (173, 216, 230)  # Light blue initially
    land_color = random.choice(land_colors)
    bird = Bird()

    while True:
        for event in pygame.event.get():
            ### Continues

        if not game_over:
            # Update bird and pipes
            bird.update()
            ### Continues

        # Drawing
        ### Continues
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
```

<details>

<summary>Full final Python output (removed thinking parts)</summary>

```python
import pygame
import random
import sys

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird Clone")
clock = pygame.time.Clock()

# Colors
pipe_colors = [(0, 100, 0), (210, 180, 140), (50, 50, 50)]
land_colors = [(139, 69, 19), (255, 255, 0)]

# Game constants
GRAVITY = 0.5
PIPE_SPEED = 5
BIRD_SIZE = 30
LAND_HEIGHT = 50
PIPE_WIDTH = 50
PIPE_GAP = 150

class Bird:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.velocity = 0
        self.shape = random.choice(['square', 'circle', 'triangle'])
        self.color = (random.randint(0, 100), random.randint(0, 100), random.randint(0, 100))
        self.rect = pygame.Rect(self.x - BIRD_SIZE//2, self.y - BIRD_SIZE//2, BIRD_SIZE, BIRD_SIZE)

    def update(self):
        self.velocity += GRAVITY
        self.y += self.velocity
        self.rect.y = self.y - BIRD_SIZE//2
        self.rect.x = self.x - BIRD_SIZE//2  # Keep x centered

    def draw(self):
        if self.shape == 'square':
            pygame.draw.rect(screen, self.color, self.rect)
        elif self.shape == 'circle':
            pygame.draw.circle(screen, self.color, (self.rect.centerx, self.rect.centery), BIRD_SIZE//2)
        elif self.shape == 'triangle':
            points = [
                (self.rect.centerx, self.rect.top),
                (self.rect.left, self.rect.bottom),
                (self.rect.right, self.rect.bottom)
            ]
            pygame.draw.polygon(screen, self.color, points)

def spawn_pipe():
    pipe_x = WIDTH
    top_height = random.randint(50, HEIGHT - PIPE_GAP - LAND_HEIGHT)
    rect_top = pygame.Rect(pipe_x, 0, PIPE_WIDTH, top_height)
    bottom_y = top_height + PIPE_GAP
    bottom_height = (HEIGHT - LAND_HEIGHT) - bottom_y
    rect_bottom = pygame.Rect(pipe_x, bottom_y, PIPE_WIDTH, bottom_height)
    color = random.choice(pipe_colors)
    return {
        'rect_top': rect_top,
        'rect_bottom': rect_bottom,
        'color': color,
        'scored': False
    }

def main():
    best_score = 0
    current_score = 0
    game_over = False
    pipes = []
    first_time = True  # Track first game play

    # Initial setup
    background_color = (173, 216, 230)  # Light blue initially
    land_color = random.choice(land_colors)
    bird = Bird()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_SPACE:
                    if game_over:
                        # Reset the game
                        bird = Bird()
                        pipes.clear()
                        current_score = 0
                        if first_time:
                            # First restart after initial game over
                            background_color = (random.randint(200, 255), random.randint(200, 255), random.randint(200, 255))
                            first_time = False
                        else:
                            background_color = (random.randint(200, 255), random.randint(200, 255), random.randint(200, 255))
                        land_color = random.choice(land_colors)
                        game_over = False
                    else:
                        # Jump the bird
                        bird.velocity = -15  # Initial upward velocity

        if not game_over:
            # Update bird and pipes
            bird.update()

            # Move pipes left
            remove_pipes = []
            for pipe in pipes:
                pipe['rect_top'].x -= PIPE_SPEED
                pipe['rect_bottom'].x -= PIPE_SPEED
                # Check if bird passed the pipe
                if not pipe['scored'] and bird.rect.x > pipe['rect_top'].right:
                    current_score += 1
                    pipe['scored'] = True
                # Check if pipe is offscreen
                if pipe['rect_top'].right < 0:
                    remove_pipes.append(pipe)
            # Remove offscreen pipes
            for p in remove_pipes:
                pipes.remove(p)

            # Spawn new pipe if needed
            if not pipes or pipes[-1]['rect_top'].x < WIDTH - 200:
                pipes.append(spawn_pipe())

            # Check collisions
            land_rect = pygame.Rect(0, HEIGHT - LAND_HEIGHT, WIDTH, LAND_HEIGHT)
            bird_rect = bird.rect
            # Check pipes
            for pipe in pipes:
                if bird_rect.colliderect(pipe['rect_top']) or bird_rect.colliderect(pipe['rect_bottom']):
                    game_over = True
                    break
            # Check land and top
            if bird_rect.bottom >= land_rect.top or bird_rect.top <= 0:
                game_over = True

            if game_over:
                if current_score > best_score:
                    best_score = current_score

        # Drawing
        screen.fill(background_color)
        # Draw pipes
        for pipe in pipes:
            pygame.draw.rect(screen, pipe['color'], pipe['rect_top'])
            pygame.draw.rect(screen, pipe['color'], pipe['rect_bottom'])
        # Draw land
        pygame.draw.rect(screen, land_color, (0, HEIGHT - LAND_HEIGHT, WIDTH, LAND_HEIGHT))
        # Draw bird
        bird.draw()
        # Draw score
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f'Score: {current_score}', True, (0, 0, 0))
        screen.blit(score_text, (WIDTH - 150, 10))
        # Game over screen
        if game_over:
            over_text = font.render('Game Over!', True, (255, 0, 0))
            best_text = font.render(f'Best: {best_score}', True, (255, 0, 0))
            restart_text = font.render('Press SPACE to restart', True, (255, 0, 0))
            screen.blit(over_text, (WIDTH//2 - 70, HEIGHT//2 - 30))
            screen.blit(best_text, (WIDTH//2 - 50, HEIGHT//2 + 10))
            screen.blit(restart_text, (WIDTH//2 - 100, HEIGHT//2 + 50))

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
```

</details>

5. Test without fixes — remove `--samplers "top_k;top_p;min_p;temperature;dry;typ_p;xtc"` — output saves to `Q4_K_M_no_samplers.txt`:

```bash
./llama.cpp/llama-cli \
    --model unsloth-QwQ-32B-GGUF/QwQ-32B-Q4_K_M.gguf \
    --threads 32 \
    --ctx-size 16384 \
    --n-gpu-layers 99 \
    --seed 3407 \
    --prio 2 \
    --temp 0.6 \
    --repeat-penalty 1.1 \
    --dry-multiplier 0.5 \
    --min-p 0.01 \
    --top-k 40 \
    --top-p 0.95 \
    -no-cnv \
    --prompt "<|im_start|>user\nCreate a Flappy Bird game in Python. You must include these things:\n1. You must use pygame.\n2. The background color should be randomly chosen and is a light shade. Start with a light blue color.\n3. Pressing SPACE multiple times will accelerate the bird.\n4. The bird's shape should be randomly chosen as a square, circle or triangle. The color should be randomly chosen as a dark color.\n5. Place on the bottom some land colored as dark brown or yellow chosen randomly.\n6. Make a score shown on the top right side. Increment if you pass pipes and don't hit them.\n7. Make randomly spaced pipes with enough space. Color them randomly as dark green or light brown or a dark gray shade.\n8. When you lose, show the best score. Make the text inside the screen. Pressing q or Esc will quit the game. Restarting is pressing SPACE again.\nThe final game should be inside a markdown section in Python. Check your code for errors and fix them before the final markdown section.<|im_end|>\n<|im_start|>assistant\n{}\n"  \
        2>&1 | tee Q4_K_M_no_samplers.txt
```

Result: looping with **incorrect Python syntax**. Example — line 39 has a NameError:

```python
import pygame
import random

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
GROUND_HEIGHT = 20
GRAVITY = 0.7
PIPE_SPEED = -3
BIRD_SIZE = 45
MIN_GAP = 130
MAX_GAP = 200
PIPE_COLORS = [(0, 96, 0), (205, 133, 63), (89, 97, 107)]
DARK_BROWN = (94, 72, 4)
YELLOW = (252, 228, 6)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

def random_light_color():
    return (
        random.randint(180, 230),
        random.randint(190, 300),
        random.randint(250, 255)
    )

def reset_game():
    global bird_x, bird_y
    global pipes, score
    global background_color, land_color
    global bird_shape, bird_color

    # Bird properties
    bird_x = WIDTH * 0.3
    bird_y = HEIGHT // 2
    bird_vel = -5  # Initial upward thrust

    pipes.clear() ### <<< NameError: name 'pipes' is not defined. Did you forget to import 'pipes'?
```

With `--repeat-penalty 1.5` it gets worse:

```python
import pygame
from random import randint  # For generating colors/shapes/positions randomly
pygame.init()

# Constants:
WIDTH, HEIGHT =456 ,702   #
BACKGROUND_COLOR_LIGHTS=['lightskyblue']
GAP_SIZE=189           #

BIRD_RADIUS=3.
PIPE_SPEED=- ( )    ?
class Game():
def __init__(self):
        self.screen_size=( )

def reset_game_vars():
    global current_scor e
   # set to zero and other initial states.

# Main game loop:
while running :
     for event in pygame.event.get() :
        if quit ... etc

pygame.quit()
print("Code is simplified. Due time constraints, full working version requires further implementation.")
```

6. BF16 (full precision) also fails without the `--samplers` fix when using Repetition Penalty — the issue is not quantization-specific.

## Still Doesn't Work? Try Min_p = 0.1, Temperature = 1.5

Per the [Min_p paper](https://arxiv.org/pdf/2407.01082), for more creative/diverse output with fewer repetitions, try disabling top_p and top_k:

```bash
./llama.cpp/llama-cli --model unsloth-QwQ-32B-GGUF/QwQ-32B-Q4_K_M.gguf \
    --threads 32 --n-gpu-layers 99 \
    --ctx-size 16384 \
    --temp 1.5 \
    --min-p 0.1 \
    --top-k 0 \
    --top-p 1.0 \
    -no-cnv \
    --prompt "<|im_start|>user\nCreate a Flappy Bird game in Python. You must include these things:\n1. You must use pygame.\n2. The background color should be randomly chosen and is a light shade. Start with a light blue color.\n3. Pressing SPACE multiple times will accelerate the bird.\n4. The bird's shape should be randomly chosen as a square, circle or triangle. The color should be randomly chosen as a dark color.\n5. Place on the bottom some land colored as dark brown or yellow chosen randomly.\n6. Make a score shown on the top right side. Increment if you pass pipes and don't hit them.\n7. Make randomly spaced pipes with enough space. Color them randomly as dark green or light brown or a dark gray shade.\n8. When you lose, show the best score. Make the text inside the screen. Pressing q or Esc will quit the game. Restarting is pressing SPACE again.\nThe final game should be inside a markdown section in Python. Check your code for errors and fix them before the final markdown section.<|im_end|>\n<|im_start|>assistant\n{}\n"
```

Alternative — disable `min_p` directly (llama.cpp defaults to `min_p = 0.1`):

```bash
./llama.cpp/llama-cli --model unsloth-QwQ-32B-GGUF/QwQ-32B-Q4_K_M.gguf \
    --threads 32 --n-gpu-layers 99 \
    --ctx-size 16384 \
    --temp 0.6 \
    --min-p 0.0 \
    --top-k 40 \
    --top-p 0.95 \
    -no-cnv \
    --prompt "<|im_start|>user\nCreate a Flappy Bird game in Python. You must include these things:\n1. You must use pygame.\n2. The background color should be randomly chosen and is a light shade. Start with a light blue color.\n3. Pressing SPACE multiple times will accelerate the bird.\n4. The bird's shape should be randomly chosen as a square, circle or triangle. The color should be randomly chosen as a dark color.\n5. Place on the bottom some land colored as dark brown or yellow chosen randomly.\n6. Make a score shown on the top right side. Increment if you pass pipes and don't hit them.\n7. Make randomly spaced pipes with enough space. Color them randomly as dark green or light brown or a dark gray shade.\n8. When you lose, show the best score. Make the text inside the screen. Pressing q or Esc will quit the game. Restarting is pressing SPACE again.\nThe final game should be inside a markdown section in Python. Check your code for errors and fix them before the final markdown section.<|im_end|>\n<|im_start|>assistant\n{}\n"
```

## Token Not Shown

Some systems don't output thinking traces correctly because `{}` is added in the chat template by default. Edit the Jinja template — remove `{}\n` at the end:

Change: `{%- if add_generation_prompt %} {{- '<|im_start|>assistant\n{}\n' }} {%- endif %}`
To: `{%- if add_generation_prompt %} {{- '<|im_start|>assistant\n' }} {%- endif %}`

The model must then manually add `{}` during inference, which may not always succeed. DeepSeek also edited all models to default-add a `{}` token.

## Extra Notes

Investigations that were ruled out:

1. **Context length / YaRN** — QwQ's native context is 32K with YaRN extension to 128K, not natively 128K:

```json
{
  ...,
  "rope_scaling": {
    "factor": 4.0,
    "original_max_position_embeddings": 32768,
    "type": "yarn"
  }
}
```

Overriding llama.cpp's YaRN handling did not help:

```bash
--override-kv qwen2.context_length=int:131072 \
--override-kv qwen2.rope.scaling.type=str:yarn \
--override-kv qwen2.rope.scaling.factor=float:4 \
--override-kv qwen2.rope.scaling.original_context_length=int:32768 \
--override-kv qwen2.rope.scaling.attn_factor=float:1.13862943649292 \
```

2. **RMS Layernorm epsilon** — tested changing from 1e-5 to 1e-6 (per [Qwen2.5-32B-Instruct](https://huggingface.co/Qwen/Qwen2.5-32B-Instruct/blob/main/config.json) `rms_norm_eps=1e-06` vs [Qwen2.5-32B](https://huggingface.co/Qwen/Qwen2.5-32B/blob/main/config.json) `rms_norm_eps=1e-05`). Did not help:

```bash
--override-kv qwen2.attention.layer_norm_rms_epsilon=float:0.000001 \
```

3. **Tokenizer ID mismatch** — tested IDs between llama.cpp and Transformers per [@kalomaze](https://x.com/kalomaze/status/1897875332230779138). They matched — not the cause.

Experimental result files:
- [BF16 no sampling fix](https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2Fgit-blob-daa99953e0628c36fd53745a4b786206907e7d9a%2Ffile_BF16_no_samplers.txt?alt=media)
- [BF16 with sampling fix](https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2Fgit-blob-52f35bdaa5b1d7c9c19e943f224f049de2f0555f%2Ffile_BF16_yes_samplers.txt?alt=media)
- [Q4_K_M no sampling fix](https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2Fgit-blob-276ff61d8749856abacdd33f38e73f9782a516fd%2Ffinal_Q4_K_M_no_samplers.txt?alt=media)
- [Q4_K_M with sampling fix](https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2Fgit-blob-ea3905fe9ce08d0fdf291ee2a32eaa6958759547%2Ffinal_Q4_K_M_yes_samplers.txt?alt=media)

## Tokenizer Bug Fixes

- **PAD token** should be `"<|vision_pad|>"` rather than empty. Updated in [Unsloth tokenizer_config.json](https://huggingface.co/unsloth/QwQ-32B/blob/main/tokenizer_config.json):

```
"eos_token": "<|im_end|>",
"pad_token": "<|vision_pad|>",
```

## Dynamic 4-bit Quants

Dynamic 4-bit quants increase accuracy vs naive 4-bit quantizations. Uploaded to [Unsloth QwQ-32B-unsloth-bnb-4bit](https://huggingface.co/unsloth/QwQ-32B-unsloth-bnb-4bit).

Since vLLM 0.7.3 (2025-02-20, [release](https://github.com/vllm-project/vllm/releases/tag/v0.7.3)), vLLM supports loading Unsloth dynamic 4-bit quants.

All GGUFs at [Unsloth QwQ-32B-GGUF](https://huggingface.co/unsloth/QwQ-32B-GGUF).

#llm #qwq-32b #llama-cpp #ollama #inference

---
title: How to Run and Deploy LLMs on your iOS or Android Phone
url: https://unsloth.ai/docs/basics/inference-and-deployment/deploy-llms-phone.md
source: llms
fetched_at: 2026-04-27T18:14:53.760374217-03:00
rendered_js: false
word_count: 2549
summary: This document provides a comprehensive guide on how to train and then deploy Large Language Models (LLMs), specifically Qwen3, onto mobile devices like iOS and Android phones using frameworks from Unsloth, TorchAO, and ExecuTorch.
tags:
    - llm-deployment
    - ios-android
    - pytorch-qat
    - executorch
    - unsloth
    - edge-ai
    - mobile-nn
category: tutorial
optimized: true
optimized_at: 2026-04-27T21:36:00Z
---

# How to Run and Deploy LLMs on your iOS or Android Phone

Train LLMs with Unsloth + TorchAO + ExecuTorch, then deploy locally to Android/iPhone. Uses [Quantization-Aware Training (QAT)](108-blog-quantization-aware-training-qat) then ExecuTorch export.

**Key results:**
- Qwen3-0.6B on Pixel 8 / iPhone 15 Pro at ~40 tokens/s
- QAT via TorchAO recovers ~70% of accuracy vs naive PTQ
- Privacy-first, offline, instant responses
- Same ExecuTorch tech Meta uses for Instagram/WhatsApp

**Colab notebook:** [Qwen3-0.6B Phone Deployment](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_\(0_6B\)-Phone_Deployment.ipynb)

## Training Your Model

Supported models: Qwen3, Gemma3, Llama3, Qwen2.5, Phi4, and more.

### Install dependencies

```bash
pip install --upgrade unsloth unsloth_zoo
pip install torchao==0.14.0 executorch pytorch_tokenizers
```

### Load model with QAT

Use `qat_scheme = "phone-deployment"` to enable phone deployment. Under the hood this uses `int8-int4` -- simulates INT8 dynamic activation quantization with INT4 weight quantization for Linear layers during training (fake quantization, computations in 16-bit). Post-training, the model is converted to real quantized form, retaining better accuracy than naive PTQ.

```python
from unsloth import FastLanguageModel
import torch
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "unsloth/Qwen3-0.6B",
    max_seq_length = 1024,
    full_finetuning = True,
    qat_scheme = "phone-deployment", # Flag for phone deployment
)
```

### Export to .pte via ExecuTorch

After finetuning (see [Colab notebook](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_\(0_6B\)-Phone_Deployment.ipynb)):

```bash
# Convert weight checkpoint state dict keys for ExecuTorch
python -m executorch.examples.models.qwen3.convert_weights "phone_model" pytorch_model_converted.bin
# Download model config
curl -L -o 0.6B_config.json https://raw.githubusercontent.com/pytorch/executorch/main/examples/models/qwen3/config/0_6b_config.json
# Export to ExecuTorch pte file
python -m executorch.examples.models.llama.export_llama \
    --model "qwen3_0_6b" \
    --checkpoint pytorch_model_converted.bin \
    --params 0.6B_config.json \
    --output_name qwen3_0.6B_model.pte \
    -kv --use_sdpa_with_kv_cache -X --xnnpack-extended-ops \
    --max_context_length 1024 --max_seq_length 128 --dtype fp32 \
    --metadata '{"get_bos_id":199999, "get_eos_ids":[200020,199999]}'
```

Output: `qwen3_0.6B_model.pte` (~472MB).

## iOS Deployment

Tested on iPhone 16 Pro; works on other iPhones. Requires macOS with Xcode 15+.

### macOS Development Environment Setup

1. Install Xcode 15+ from Mac App Store
2. Verify: `xcode-select -p`
3. Install command line tools and accept license:
   1. `xcode-select --install`
   2. `sudo xcodebuild -license accept`
4. Launch Xcode, install additional components when prompted
5. Select iOS 18 platform for simulator access

> [!warning] First Xcode launch is crucial -- do not skip extra component installations.
> See [downloading components](https://developer.apple.com/documentation/xcode/downloading-and-installing-additional-xcode-components) and [adding simulators](https://developer.apple.com/documentation/safari-developer-tools/adding-additional-simulators).

**Verify:** `xcode-select -p` should print a path. If not, repeat step 3.

### Apple Developer Account Setup

> [!info] Skip this section if using iOS Simulator only. Paid developer account required only for physical iPhone deployment.

1. Create Apple ID at [support.apple.com](https://support.apple.com/en-us/108647?device-type=iphone)
2. Add account to Xcode: Xcode > Settings > Accounts > + > sign in
3. Enroll in [Apple Developer Program](https://developer.apple.com) -- ExecuTorch requires `increased-memory-limit` capability (paid account only)

### Setup the ExecuTorch Demo App

**Download:**

```bash
curl -L https://github.com/meta-pytorch/executorch-examples/archive/main.tar.gz | \
  tar -xz --strip-components=2 executorch-examples-main/llm/apple
```

**Open in Xcode:**

1. Open `apple/etLLM.xcodeproj`
2. Select `iPhone 16 Pro` Simulator as target
3. Hit Play to build and run (app launches but has no model yet)

### Deploying to Simulator

No developer account needed.

1. Stop simulator in Xcode
2. Download `qwen3_0.6B_model.pte` and `tokenizer.json`
3. In simulator: Files App > Browse > On My iPhone > create folder `Qwen3test`
4. Find simulator folder: `find ~/Library/Developer/CoreSimulator/Devices/ -type d -iname "*Qwen3test*"`
5. Copy files:

```bash
cp tokenizer.json /path/to/Qwen3test/tokenizer.json
cp qwen3_0.6B_model.pte /path/to/Qwen3test/qwen3_model.pte
```

6. Launch etLLM app, load model and tokenizer from `Qwen3test`, start chatting

### Deploying to Physical iPhone

**Initial Device Setup:**

1. Connect iPhone via USB, tap "Trust This Device"
2. Xcode > Window > Devices and Simulators, wait for device to appear

**Configure Xcode Signing:**

1. Add Apple Account: Xcode > Settings > Accounts > +
2. Click etLLM project (blue icon) in navigator
3. Select etLLM under TARGETS > Signing & Capabilities
4. Check "Automatically manage signing", select Team

> [!warning] Change Bundle Identifier to something unique (e.g., `com.yourname.etLLM`). Fixes 99% of provisioning profile errors.

**Add Required Capability:**

Signing & Capabilities > + Capability > "Increased Memory Limit"

**Build & Run:**

1. Select physical iPhone from device selector
2. Hit Play or Cmd+R

**Trust Developer Certificate** (first build will fail -- expected):

1. iPhone > Settings > Privacy & Security > Developer Mode > On
2. Accept notices, restart device
3. Return to Xcode, hit Play again

> [!warning] Developer Mode allows Xcode to install apps on iPhone.

**Transfer Model Files:**

1. App running > Mac Finder > iPhone sidebar > Files tab > expand etLLM
2. Drag and drop `.pte` and `tokenizer.json` into the folder (may take a few minutes)
3. Switch to etLLM app on iPhone, load model and tokenizer, start chatting

## Android Deployment

Tested on Pixel 8; works on other Android phones. Uses Linux/Mac command line (no Android Studio required).

### Requirements

- Java 17 (Java 21 may cause build issues)
- Git, wget/curl
- Android Command Line Tools
- [adb](https://www.xda-developers.com/install-adb-windows-macos-linux/) installed and set up

**Verify Java:**

```bash
java -version  # Should output: openjdk version "17.0.x"
```

If mismatch, install on Ubuntu/Debian:

```bash
sudo apt install openjdk-17-jdk
export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
export PATH=$JAVA_HOME/bin:$PATH
```

### Step 1: Install Android SDK & NDK

```bash
mkdir -p ~/android-sdk/cmdline-tools
cd ~/android-sdk
wget https://dl.google.com/android/repository/commandlinetools-linux-11076708_latest.zip
unzip commandlinetools-linux-*.zip -d cmdline-tools
mv cmdline-tools/cmdline-tools cmdline-tools/latest
```

### Step 2: Configure Environment Variables

Add to `~/.bashrc` or `~/.zshrc`:

```bash
export ANDROID_HOME=$HOME/android-sdk
export PATH=$ANDROID_HOME/cmdline-tools/latest/bin:$PATH
export PATH=$ANDROID_HOME/platform-tools:$PATH
```

Reload: `source ~/.zshrc` (or `~/.bashrc`)

### Step 3: Install SDK Components

ExecuTorch requires specific NDK versions:

```bash
yes | sdkmanager --licenses
sdkmanager "platforms;android-34" "platform-tools" "build-tools;34.0.0" "ndk;25.0.8775105"
export ANDROID_NDK=$ANDROID_HOME/ndk/25.0.8775105
```

### Step 4: Get the Code

```bash
cd ~
git clone https://github.com/meta-pytorch/executorch-examples.git
cd executorch-examples
```

### Step 5: Fix Common Compilation Issues

**"SDK Location not found":**

```bash
echo "sdk.dir=$HOME/android-sdk" > llm/android/LlamaDemo/local.properties
```

**`cannot find symbol` error (deprecated `getDetailedError()`):**

```bash
sed -i 's/e.getDetailedError()/e.getMessage()/g' llm/android/LlamaDemo/app/src/main/java/com/example/executorchllamademo/MainActivity.java
```

### Step 6: Build the APK

```bash
cd llm/android/LlamaDemo
export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
./gradlew :app:assembleDebug
```

Output: `app/build/outputs/apk/debug/app-debug.apk`

### Step 7: Install on Device

**Option A -- ADB (wired/wireless):**

```bash
adb install -r app/build/outputs/apk/debug/app-debug.apk
```

**Option B -- Direct file transfer:** Upload APK somewhere, download on phone, tap to install (enable "Install from unknown sources" if prompted).

### Step 8: Transfer Model Files

The app needs `.pte` model and tokenizer files in a directory not accessible via regular file managers. Use `adb`:

```bash
adb devices  # Verify connected
adb shell mkdir -p /data/local/tmp/llama
adb shell chmod 777 /data/local/tmp/llama
adb push <path_to_tokenizer.json> /data/local/tmp/llama
adb push <path_to_model.pte> /data/local/tmp/llama
```

Then in the `executorchllamademo` app:

1. Tap gear icon (Settings)
2. Tap arrow next to Model > select `.pte` file
3. Tap arrow next to Tokenizer > select tokenizer file
4. Select model type (e.g., Qwen3)
5. Tap "Load Model"
6. Wait for loading, then chat

### Troubleshooting

- **Build fails?** `java -version` must be 17
- **Model not loading?** Select both `.pte` AND tokenizer
- **App crashing?** `.pte` must be exported for ExecuTorch (usually XNNPACK backend for CPU)
- **Blank model dialog?** ADB push likely failed -- redo

## ExecuTorch at Scale

ExecuTorch [powers on-device ML for billions](https://engineering.fb.com/2025/07/28/android/executorch-on-device-ml-meta-family-of-apps/) on Instagram, WhatsApp, Messenger, and Facebook. Supports 12+ hardware backends across Apple, Qualcomm, ARM, Meta Quest 3, and Ray-Bans.

## Other Model Support

- All Qwen3 dense models ([Qwen3-0.6B](https://huggingface.co/unsloth/Qwen3-0.6B), [Qwen3-4B](https://huggingface.co/unsloth/Qwen3-4B), [Qwen3-32B](https://huggingface.co/unsloth/Qwen3-32B))
- All Gemma 3 models ([Gemma3-270M](https://huggingface.co/unsloth/gemma-3-270m-it), [Gemma3-4B](https://huggingface.co/unsloth/gemma-3-4b-it), [Gemma3-27B](https://huggingface.co/unsloth/gemma-3-27b-it))
- All Llama 3 models ([Llama 3.1 8B](https://huggingface.co/unsloth/Llama-3.1-8B-Instruct), [Llama 3.3 70B Instruct](https://huggingface.co/unsloth/Llama-3.3-70B-Instruct))
- Qwen 2.5, Phi 4 Mini, and more

Customize the [Colab notebook](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_\(0_6B\)-Phone_Deployment.ipynb) for any supported model. See [[073-get-started-unsloth-notebooks|Unsloth Notebooks]] for all notebooks.

#tts #llm-deployment #mobile #edge-ai #executorch

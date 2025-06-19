# OCR-GPT Assistant

![CI](https://github.com/tennyros/ocr-gpt-assistant/actions/workflows/ci.yml/badge.svg?branch=dev)
![Python](https://img.shields.io/badge/python-3.7%2B-blue)
![License](https://img.shields.io/github/license/tennyros/ocr-gpt-assistant)
![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)
![Requirements Status](https://img.shields.io/badge/requirements-up%20to%20date-brightgreen)

A tool for capturing screen text and analyzing it using OCR and Ollama LLM.

## Features

- Screen capture and OCR text recognition
- Text analysis using Ollama LLM
- Desktop notifications (Linux)
- Automatic Tesseract installation check
- Configuration through environment variables

## Requirements

- Python 3.7+ (use `python3` command)
- Tesseract OCR (automatically checked at startup)
  - Windows: Download from [UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki)
  - Linux: `sudo apt install tesseract-ocr`
  - macOS: `brew install tesseract`
- Ollama running locally or accessible via network
- For Linux notifications: `libnotify-bin`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/tennyros/ocr-gpt-assistant.git
   cd ocr-gpt-assistant
   ```

2. Install system dependencies (Linux only):
   ```bash
   sudo apt install libnotify-bin  # For desktop notifications
   ```

3. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Copy `.env.sample` to `.env` and adjust settings as needed:
   ```bash
   cp .env.sample .env
   ```

Note: The program will check for Tesseract OCR at startup and provide installation 
instructions if needed.

## Configuration

Edit the `.env` file to configure:

```ini
# OCR settings
OCR_LANGUAGE=eng

# Interval between screen captures (in seconds)
CAPTURE_INTERVAL=5

# Ollama settings
OLLAMA_URL=http://localhost:11434
OLLAMA_MODEL=deepseek-coder:6.7b

# Monitor bounding boxes (left, upper, right, lower)
LEFT_MONITOR_BBOX=0,0,2560,1440
RIGHT_MONITOR_BBOX=2560,0,5120,1440

# Enable smart capture (True/False)
SMART_CAPTURE=False

# Monitor bounding boxes for hotkeys (format: hotkey:left,top,right,bottom;...)
MONITOR_BBOXES=ctrl+1:0,0,2560,1440;ctrl+2:2560,0,5120,1440
```

## Usage Modes

### Interval Mode (automatic capture)
Captures screen at regular intervals:

```bash
# Capture full screen
python3 run.py --mode interval --screen all

# Capture left monitor only
python3 run.py --mode interval --screen left

# Capture right monitor only
python3 run.py --mode interval --screen right
```

### Hotkey Mode
Capture specific screen regions using hotkeys:

```bash
python3 run.py --mode hotkey
```

Available hotkeys:
- `Ctrl+1`: Capture left monitor
- `Ctrl+2`: Capture right monitor

## Usage

Run the script:

```bash
python main.py
```

The program will:
1. Wait for the specified delay (if configured)
2. Capture your entire screen
3. Perform OCR to recognize text
4. Send recognized text to Ollama for analysis
5. Display both the recognized text and analysis results

## Project Structure

- `main.py` - Main entry point
- `config.py` - Configuration settings
- `core/` - Core functionality
  - `ocr_reader.py` - OCR processing
  - `screen_capture.py` - Screen capture utilities
  - `text_processor.py` - Text processing and analysis
- `integrations/` - External services integration
  - `ollama_client.py` - Ollama API client

## License

MIT
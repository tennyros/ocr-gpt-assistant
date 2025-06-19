# OCR-GPT Assistant

A tool for capturing screen text and analyzing it using OCR and Ollama LLM.

## Features

- Screen capture and OCR text recognition
- Text analysis using Ollama LLM
- Desktop notifications (Linux)
- Automatic Tesseract installation check
- Configuration through environment variables

## Requirements

- Python 3.7+
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
OCR_LANGUAGE=eng    # OCR language(s), e.g., eng+rus for multiple
CAPTURE_DELAY=0     # Delay in seconds before capture

# Ollama settings
OLLAMA_URL=http://localhost:11434  # Ollama API URL
OLLAMA_MODEL=deepseek-coder:6.7b   # Model to use
```

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
# OCR-GPT Assistant

A simple tool for capturing and recognizing text from your screen using OCR.

## Requirements

- Python 3.7+
- Tesseract OCR must be installed on your system:
  - Windows: Download from [UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki)
  - Linux: `sudo apt install tesseract-ocr`
  - macOS: `brew install tesseract`

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd ocr-gpt-assistant
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Create a `.env` file in the project root (optional):
```ini
OCR_LANGUAGE=eng    # OCR language(s), e.g., eng+rus for multiple
CAPTURE_DELAY=0     # Delay in seconds before capture
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
4. Display the recognized text in the console

## Project Structure

- `main.py` - Main entry point
- `config.py` - Configuration settings
- `core/` - Core functionality
  - `ocr_reader.py` - OCR processing
  - `screen_capture.py` - Screen capture utilities

## License

MIT
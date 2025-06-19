"""
OCR functionality module
"""

import logging
import sys
import shutil
import platform
import pytesseract
from PIL import Image
from config import OCR_LANGUAGE


def check_tesseract_installed() -> bool:
    """
    Check if Tesseract is installed and provide installation
    instructions if not

    Returns:
        bool: True if Tesseract is installed, False otherwise
    """
    if shutil.which("tesseract") is None:
        system = platform.system().lower()

        print("\nTesseract OCR is not installed!")
        print("\nInstallation instructions:")

        if system == "windows":
            print(
                "1. Download installer from: "
                "https://github.com/UB-Mannheim/tesseract/wiki"
            )
            print("2. Run the installer and follow the instructions")
            print(
                "3. Add Tesseract to PATH or set TESSERACT_CMD"
                "in your environment"
            )

        elif system == "darwin":  # macOS
            print("Install using Homebrew:")
            print("  brew install tesseract")

        elif system == "linux":
            print("Install using apt (Ubuntu/Debian):")
            print("  sudo apt install tesseract-ocr")
            print("  sudo apt install tesseract-ocr-eng")  # for English
            print("  sudo apt install tesseract-ocr-rus")  # for Russian

        else:
            print(
                "Please visit https://tesseract-ocr.github.io/tessdoc/"
                "Installation.html"
            )

        return False

    return True


def extract_text(image: Image.Image) -> str:
    """
    Extract text from an image using OCR

    Args:
        image: PIL Image object to process

    Returns:
        str: Recognized text
    """
    if not check_tesseract_installed():
        sys.exit(1)

    try:
        return pytesseract.image_to_string(image, lang=OCR_LANGUAGE)
    except Exception as e:
        logging.error(f"OCR error: {e}")
        return ""

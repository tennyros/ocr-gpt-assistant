"""
OCR functionality module
"""
import logging
import pytesseract
from PIL import Image
from config import OCR_LANGUAGE

def extract_text(image: Image) -> str:
    """
    Extract text from an image using OCR.
    
    Args:
        image: PIL Image object to process
        
    Returns:
        str: Recognized text
    """
    try:
        return pytesseract.image_to_string(image, lang=OCR_LANGUAGE)
    except Exception as e:
        logging.error(f"OCR error: {e}")
        return ""
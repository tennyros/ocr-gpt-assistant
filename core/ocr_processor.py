"""
Text analysis from image and interaction with Ollama
"""
import logging
from .ocr_reader import extract_text
from integrations.ollama_client import ask_ollama
from .notifier import Notifier

def analyze_text_from_image(data) -> None:
    """
    Recognizes text from an image or analyzes already extracted text,
    sends it to Ollama, and notifies the user.
    
    Args:
        data: PIL.Image object or string with text
    """
    notifier = Notifier()
    
    # Handle both image and pre-extracted text
    if isinstance(data, str):
        text = data.strip()
    else:
        text = extract_text(data).strip()
        
    logging.debug(f"OCR text: {repr(text)}")

    if not text:
        logging.warning("No text recognized")
        notifier.notify("OCR Result", "No text was recognized")
        return

    logging.info(f"Text detected:\n{text}")
    logging.debug("Sending to Ollama...")

    try:
        answer = ask_ollama(text)
        logging.info("Model response:")
        logging.info(answer)
        notifier.notify("Analysis Complete", answer[:100] + "..." if len(answer) > 100 else answer)
    except Exception as e:
        error_msg = f"Error communicating with Ollama: {e}"
        logging.error(error_msg)
        notifier.notify("Analysis Failed", error_msg)
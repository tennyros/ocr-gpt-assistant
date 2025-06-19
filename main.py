"""
Basic screen capture and OCR functionality
"""
import logging
from time import sleep
from core.screen_capture import capture_screen
from core.ocr_reader import extract_text
from config import CAPTURE_DELAY

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s: %(message)s')

def main():
    try:
        # Optional delay before capture
        if CAPTURE_DELAY > 0:
            logging.info(f"Waiting {CAPTURE_DELAY} seconds before capture...")
            sleep(CAPTURE_DELAY)
        
        # Capture the screen
        logging.info("Capturing screen...")
        image = capture_screen()
        if image is None:
            return
        
        # Recognize text
        logging.info("Performing OCR...")
        text = extract_text(image)
        
        if text.strip():
            print("\nRecognized text:")
            print("-" * 40)
            print(text)
        else:
            print("No text was recognized")
            
    except Exception as e:
        logging.error(f"Error: {e}")

if __name__ == "__main__":
    main()
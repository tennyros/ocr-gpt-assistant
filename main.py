"""
OCR-GPT Assistant main module
"""
import logging
from time import sleep
from core.screen_capture import capture_screen
from core.ocr_reader import extract_text
from core.text_processor import TextProcessor
from config import CAPTURE_DELAY

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s: %(message)s')

def main():
    try:
        # Initialize text processor
        processor = TextProcessor()
        
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
        
        if not text.strip():
            print("No text was recognized")
            return
            
        print("\nRecognized text:")
        print("-" * 40)
        print(text)
        
        # Process text with Ollama
        logging.info("Analyzing text with Ollama...")
        analysis = processor.process_text(text)
        
        if analysis:
            print("\nAnalysis result:")
            print("-" * 40)
            print(analysis)
        else:
            print("\nFailed to analyze text")
            
    except Exception as e:
        logging.error(f"Error: {e}")

if __name__ == "__main__":
    main()
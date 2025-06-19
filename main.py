"""
OCR-GPT Assistant main module
"""
import logging
from time import sleep
from core.screen_capture import capture_screen
from core.ocr_reader import extract_text
from core.text_processor import TextProcessor
from core.notifier import Notifier
from config import CAPTURE_DELAY

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s: %(message)s')

def main():
    try:
        # Initialize components
        processor = TextProcessor()
        notifier = Notifier()
        
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
            notifier.notify("OCR Result", "No text was recognized")
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
            notifier.notify("Analysis Complete", "Text has been analyzed successfully")
        else:
            notifier.notify("Analysis Failed", "Failed to analyze text with Ollama")
            
    except Exception as e:
        logging.error(f"Error: {e}")
        notifier.notify("Error", str(e))

if __name__ == "__main__":
    main()
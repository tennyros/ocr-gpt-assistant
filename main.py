"""
OCR-GPT Assistant: main entry point (interval mode)
"""
import logging
from time import sleep
import argparse
from core.screen_capture import capture_screen, smart_capture_text
from core.ocr_processor import analyze_text_from_image
from config import CAPTURE_INTERVAL, SMART_CAPTURE, LEFT_MONITOR_BBOX, RIGHT_MONITOR_BBOX

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s: %(message)s')

def main(screen: str = "all") -> None:
    """
    Main function for interval capture mode

    Args:
        screen: Which screen to capture ("left", "right", or "all")
    """
    logging.info(f"OCR-GPT Assistant started (interval mode, screen={screen})...")

    # Configure screen region based on mode
    if screen == "left":
        bbox = LEFT_MONITOR_BBOX
    elif screen == "right":
        bbox = RIGHT_MONITOR_BBOX
    else:
        bbox = None  # None = full screen

    try:
        while True:
            try:
                if SMART_CAPTURE:
                    text = smart_capture_text(bbox)
                    analyze_text_from_image(text)
                else:
                    image = capture_screen(bbox)
                    analyze_text_from_image(image)
            except Exception as e:
                logging.error(f"Error during capture/analyze: {e}")

            sleep(CAPTURE_INTERVAL)

    except KeyboardInterrupt:
        logging.info("Stopped by user")
    except Exception as e:
        logging.error(f"Unhandled error: {e}")

def cli():
    parser = argparse.ArgumentParser(description="OCR-GPT Assistant Interval Mode")
    parser.add_argument(
        "--screen",
        choices=["left", "right", "all"],
        default="all",
        help="Screen region to capture"
    )
    args = parser.parse_args()
    main(screen=args.screen)

if __name__ == "__main__":
    cli()
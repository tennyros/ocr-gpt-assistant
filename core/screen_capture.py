"""
Screen capture functionality
"""

import logging
import cv2
import numpy as np
from PIL import ImageGrab
import pytesseract
from typing import Optional, Tuple
from PIL.Image import Image


def capture_screen(
    bbox: Optional[Tuple[int, int, int, int]] = None,
) -> Optional[Image]:
    """
    Capture screen or specific region

    Args:
        bbox: Optional bounding box (left, top, right, bottom)

    Returns:
        PIL.Image or None: Captured image
    """
    try:
        return ImageGrab.grab(bbox=bbox)
    except Exception as e:
        logging.error(f"Screen capture error: {e}")
        return None


def smart_capture_text(
    bbox: Optional[Tuple[int, int, int, int]] = None,
) -> str:
    """
    Smart text capture with confidence filtering

    Args:
        bbox: Optional bounding box (left, top, right, bottom)

    Returns:
        str: Extracted text
    """
    try:
        screen = np.array(ImageGrab.grab(bbox=bbox))
        gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)

        # Get detailed OCR data including confidence scores
        data = pytesseract.image_to_data(
            gray, output_type=pytesseract.Output.DICT
        )

        # Filter text by confidence
        extracted = []
        for i in range(len(data["text"])):
            if int(data["conf"][i]) > 60 and data["text"][i].strip():
                extracted.append(data["text"][i])

        return " ".join(extracted)

    except Exception as e:
        logging.error(f"Smart capture error: {e}")
        return ""

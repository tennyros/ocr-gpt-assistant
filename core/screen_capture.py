"""
Screen capture functionality
"""
import logging
from PIL import ImageGrab
from typing import Optional, Tuple

def capture_screen(bbox: Optional[Tuple[int, int, int, int]] = None):
    """
    Capture the screen or a specific region.
    
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
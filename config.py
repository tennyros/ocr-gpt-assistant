"""
Configuration settings for OCR-GPT Assistant
"""
import os
from dotenv import load_dotenv
from typing import Tuple, Optional

# Load environment variables from .env file if present
load_dotenv()

# OCR settings
OCR_LANGUAGE = os.getenv("OCR_LANGUAGE", "eng+rus")  # Default languages for OCR

# Screen capture settings
CAPTURE_INTERVAL = int(os.getenv("CAPTURE_INTERVAL", "5"))  # Interval between captures in seconds

# Ollama settings
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "deepseek-coder:6.7b")

# Monitor bounding boxes (left, upper, right, lower)
def parse_bbox(env_var: str, default: str) -> Tuple[int, int, int, int]:
    parts = [int(x) for x in os.getenv(env_var, default).split(",")]
    if len(parts) != 4:
        raise ValueError(f"{env_var} must have exactly 4 comma-separated integers")
    return parts[0], parts[1], parts[2], parts[3]

LEFT_MONITOR_BBOX: Tuple[int, int, int, int] = parse_bbox("LEFT_MONITOR_BBOX", "0,0,2560,1440")
RIGHT_MONITOR_BBOX: Tuple[int, int, int, int] = parse_bbox("RIGHT_MONITOR_BBOX", "2560,0,5120,1440")

SMART_CAPTURE = os.getenv("SMART_CAPTURE", "False").lower() in ("1", "true", "yes")

MONITOR_BBOXES = {
    "ctrl+1": (0, 0, 2560, 1440),
    "ctrl+2": (2560, 0, 5120, 1440),
}
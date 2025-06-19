"""
Configuration settings for OCR-GPT Assistant
"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file if present
load_dotenv()

# OCR settings
OCR_LANGUAGE = os.getenv("OCR_LANGUAGE", "eng")  # Default language for OCR

# Screen capture settings
CAPTURE_DELAY = int(os.getenv("CAPTURE_DELAY", "0"))  # Delay before capture in seconds

# Ollama settings
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "deepseek-coder:6.7b")
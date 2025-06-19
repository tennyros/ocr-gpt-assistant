"""
Text processing and analysis module
"""
import logging
from typing import Optional
from integrations.ollama_client import OllamaClient
from config import OLLAMA_URL, OLLAMA_MODEL

class TextProcessor:
    def __init__(self):
        self.ollama = OllamaClient(OLLAMA_URL)
        
    def process_text(self, text: str) -> Optional[str]:
        """
        Process and analyze text using Ollama.
        
        Args:
            text: Text to process
            
        Returns:
            Optional[str]: Analysis result or None if failed
        """
        if not text.strip():
            logging.warning("Empty text received for processing")
            return None
            
        # Clean the text (remove extra whitespace)
        text = ' '.join(text.split())
        
        # Get analysis from Ollama
        return self.ollama.analyze_text(text, model=OLLAMA_MODEL)
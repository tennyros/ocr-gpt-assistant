"""
Ollama API client for text analysis
"""
import logging
import requests
from typing import Optional

class OllamaClient:
    def __init__(self, base_url: str = "http://localhost:11434"):
        self.base_url = base_url.rstrip('/')
        self.generate_url = f"{self.base_url}/api/generate"

    def analyze_text(self, text: str, model: str = "deepseek-coder:6.7b") -> Optional[str]:
        """
        Send text to Ollama for analysis.
        
        Args:
            text: Text to analyze
            model: Model name to use
            
        Returns:
            Optional[str]: Model's response or None if failed
        """
        try:
            response = requests.post(
                self.generate_url,
                json={
                    "model": model,
                    "prompt": text,
                    "stream": False
                }
            )
            response.raise_for_status()
            return response.json()["response"]
            
        except Exception as e:
            logging.error(f"Ollama request error: {e}")
            return None
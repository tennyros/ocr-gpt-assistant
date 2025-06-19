import unittest
from unittest.mock import patch, MagicMock, ANY
from core.text_processor import TextProcessor


class TestTextProcessor(unittest.TestCase):
    @patch("core.text_processor.OllamaClient")
    def test_empty_text_returns_none(self, mock_ollama):
        processor = TextProcessor()
        result = processor.process_text("")
        self.assertIsNone(result)
        mock_ollama.return_value.analyze_text.assert_not_called()

    @patch("core.text_processor.OllamaClient")
    def test_text_is_cleaned(self, mock_ollama):
        processor = TextProcessor()
        mock_ollama.return_value.analyze_text.return_value = "result"
        text = "   some   text   with   spaces   "
        processor.process_text(text)
        # Check that analyze_text is called with cleaned text
        mock_ollama.return_value.analyze_text.assert_called_with(
            "some text with spaces", model=ANY
        )

    @patch("core.text_processor.OllamaClient")
    def test_analyze_text_called(self, mock_ollama):
        processor = TextProcessor()
        mock_ollama.return_value.analyze_text.return_value = "result"
        result = processor.process_text("test")
        mock_ollama.return_value.analyze_text.assert_called_once()
        self.assertEqual(result, "result")


if __name__ == "__main__":
    unittest.main()

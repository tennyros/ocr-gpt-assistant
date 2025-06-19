import unittest
from unittest.mock import patch, MagicMock
from core import ocr_processor


class TestAnalyzeTextFromImage(unittest.TestCase):
    @patch("core.ocr_processor.Notifier")
    @patch("core.ocr_processor.ask_ollama")
    @patch("core.ocr_processor.extract_text")
    def test_empty_text(
        self, mock_extract_text, mock_ask_ollama, mock_notifier
    ):
        # Check behavior with empty text
        notifier_instance = mock_notifier.return_value
        ocr_processor.analyze_text_from_image("")
        notifier_instance.notify.assert_called_with(
            "OCR Result", "No text was recognized"
        )
        mock_ask_ollama.assert_not_called()

    @patch("core.ocr_processor.Notifier")
    @patch(
        "core.ocr_processor.ask_ollama", side_effect=Exception("Ollama error")
    )
    @patch("core.ocr_processor.extract_text", return_value="Some text")
    def test_ollama_error(
        self, mock_extract_text, mock_ask_ollama, mock_notifier
    ):
        # Check behavior when Ollama raises an error
        notifier_instance = mock_notifier.return_value
        ocr_processor.analyze_text_from_image(MagicMock())
        notifier_instance.notify.assert_called()
        args, kwargs = notifier_instance.notify.call_args
        self.assertIn("Analysis Failed", args[0])
        self.assertIn("Ollama error", args[1])

    @patch("core.ocr_processor.Notifier")
    @patch("core.ocr_processor.ask_ollama", return_value="Model answer")
    @patch("core.ocr_processor.extract_text", return_value="Some text")
    def test_successful_analysis(
        self, mock_extract_text, mock_ask_ollama, mock_notifier
    ):
        # Check successful analysis scenario
        notifier_instance = mock_notifier.return_value
        ocr_processor.analyze_text_from_image(MagicMock())
        notifier_instance.notify.assert_called()
        args, kwargs = notifier_instance.notify.call_args
        self.assertEqual(args[0], "Analysis Complete")
        self.assertIn("Model answer", args[1])


if __name__ == "__main__":
    unittest.main()

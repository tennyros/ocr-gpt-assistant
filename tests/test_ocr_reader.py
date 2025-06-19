import unittest
from unittest.mock import patch
from core import ocr_reader
from PIL import Image


class TestOCRReader(unittest.TestCase):
    @patch("core.ocr_reader.shutil.which", return_value="/usr/bin/tesseract")
    def test_check_tesseract_installed_true(self, mock_which):
        self.assertTrue(ocr_reader.check_tesseract_installed())

    @patch("core.ocr_reader.shutil.which", return_value=None)
    @patch("core.ocr_reader.platform.system", return_value="Linux")
    def test_check_tesseract_installed_false(self, mock_system, mock_which):
        with patch("builtins.print") as mock_print:
            self.assertFalse(ocr_reader.check_tesseract_installed())
            mock_print.assert_any_call("\nTesseract OCR is not installed!")

    @patch("core.ocr_reader.check_tesseract_installed", return_value=True)
    @patch(
        "core.ocr_reader.pytesseract.image_to_string",
        return_value="recognized text",
    )
    def test_extract_text_success(self, mock_ocr, mock_check):
        image = Image.new("RGB", (10, 10))
        result = ocr_reader.extract_text(image)
        self.assertEqual(result, "recognized text")

    @patch("core.ocr_reader.check_tesseract_installed", return_value=True)
    @patch(
        "core.ocr_reader.pytesseract.image_to_string",
        side_effect=Exception("ocr error"),
    )
    def test_extract_text_error(self, mock_ocr, mock_check):
        image = Image.new("RGB", (10, 10))
        with patch("core.ocr_reader.logging.error") as mock_log:
            result = ocr_reader.extract_text(image)
            self.assertEqual(result, "")
            mock_log.assert_called()

    @patch("core.ocr_reader.check_tesseract_installed", return_value=False)
    def test_extract_text_no_tesseract(self, mock_check):
        image = Image.new("RGB", (10, 10))
        with patch("sys.exit") as mock_exit:
            ocr_reader.extract_text(image)
            mock_exit.assert_called_with(1)


if __name__ == "__main__":
    unittest.main()

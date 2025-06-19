import unittest
from unittest.mock import patch, MagicMock
from core.notifier import Notifier


class TestNotifier(unittest.TestCase):
    def test_notify_with_notify2(self):
        mock_notify2 = MagicMock()
        with patch(
            "core.notifier.platform.system", return_value="Linux"
        ), patch.dict("sys.modules", {"notify2": mock_notify2}):
            notifier = Notifier()
            notifier.notification_system = "notify2"
            notifier.notify("Title", "Message", timeout=1234)
            mock_notify2.Notification.assert_called_with("Title", "Message")
            n = mock_notify2.Notification.return_value
            n.set_timeout.assert_called_with(1234)
            n.show.assert_called()

    def test_notify_fallback_to_print(self):
        # Симулируем ImportError при импорте notify2
        with patch(
            "core.notifier.platform.system", return_value="Linux"
        ), patch.dict("sys.modules", {"notify2": None}):
            notifier = Notifier()
            notifier.notification_system = None
            with patch("builtins.print") as mock_print:
                notifier.notify("Title", "Message")
                mock_print.assert_any_call("\n[Title]\nMessage")

    def test_notify_error_handling(self):
        mock_notify2 = MagicMock()
        mock_notify2.Notification.side_effect = Exception("notify2 error")
        with patch(
            "core.notifier.platform.system", return_value="Linux"
        ), patch.dict("sys.modules", {"notify2": mock_notify2}):
            notifier = Notifier()
            notifier.notification_system = "notify2"
            with patch("core.notifier.logging.error") as mock_log, patch(
                "builtins.print"
            ) as mock_print:
                notifier.notify("Title", "Message")
                mock_log.assert_called()
                mock_print.assert_any_call("\n[Title]\nMessage")


if __name__ == "__main__":
    unittest.main()

"""
Desktop notification module
"""

import logging
import platform
from typing import Optional


class Notifier:
    def __init__(self):
        self.notification_system = self._initialize_notifications()

    def _initialize_notifications(self) -> Optional[str]:
        """Initialize appropriate notification system based on OS"""
        system = platform.system().lower()

        if system == "linux":
            try:
                import notify2

                notify2.init("OCR-GPT Assistant")
                return "notify2"
            except ImportError:
                logging.warning(
                    "notify2 not available. Install with: pip install notify2"
                )

        return None

    def notify(self, title: str, message: str, timeout: int = 5000) -> None:
        """
        Show desktop notification

        Args:
            title: Notification title
            message: Notification message
            timeout: Notification timeout in milliseconds
        """
        try:
            if self.notification_system == "notify2":
                import notify2

                n = notify2.Notification(title, message)
                n.set_timeout(timeout)
                n.show()
            else:
                # Fallback to console
                print(f"\n[{title}]\n{message}")

        except Exception as e:
            logging.error(f"Notification error: {e}")
            print(f"\n[{title}]\n{message}")

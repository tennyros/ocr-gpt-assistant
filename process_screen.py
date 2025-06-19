"""
OCR-GPT Assistant: hotkey mode entry point
"""
import logging
from pynput import keyboard
from core.screen_capture import capture_screen, smart_capture_text
from core.ocr_processor import analyze_text_from_image
from config import MONITOR_BBOXES, SMART_CAPTURE

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s: %(message)s')

hotkey_actions = {}

# Configure actions for each monitor hotkey
for key, bbox in MONITOR_BBOXES.items():
    def make_action(bbox):
        if SMART_CAPTURE:
            return lambda: analyze_text_from_image(smart_capture_text(bbox))
        else:
            return lambda: analyze_text_from_image(capture_screen(bbox))
    hotkey_actions[key] = make_action(bbox)
    logging.info(f"Hotkey {key} assigned to region {bbox}")

current_keys = set()

# Key mapping for different platforms
key_map = {
    'ctrl': keyboard.Key.ctrl_l,
    'ctrl_r': keyboard.Key.ctrl_r,
    'shift': keyboard.Key.shift,
    'alt': keyboard.Key.alt,
    'alt_gr': keyboard.Key.alt_gr,
    'cmd': keyboard.Key.cmd,
    'win': keyboard.Key.cmd,
}

def parse_hotkey(hotkey_str):
    """Convert string hotkey to tuple of keys"""
    parts = hotkey_str.lower().split('+')
    return tuple(key_map.get(p, p) for p in parts)

hotkey_combos = {parse_hotkey(hk): action for hk, action in hotkey_actions.items()}

def on_press(key):
    current_keys.add(key)
    for combo, action in hotkey_combos.items():
        if all(k in current_keys or (isinstance(k, str) and getattr(key, 'char', None) == k) for k in combo):
            action()

def on_release(key):
    if key in current_keys:
        current_keys.remove(key)

def main() -> None:
    logging.info("OCR-GPT Assistant started (hotkey mode)...")
    logging.info("Press configured hotkeys to capture and analyze specific screen regions")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()
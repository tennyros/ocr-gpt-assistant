#!/usr/bin/env python3
"""
OCR-GPT Assistant universal launcher
"""
import argparse
import sys
from main import main as interval_main
from process_screen import main as hotkey_main

def cli():
    parser = argparse.ArgumentParser(description="OCR-GPT Assistant")
    parser.add_argument(
        "--mode",
        choices=["interval", "hotkey"],
        default="interval",
        help="Run in interval mode or hotkey mode"
    )
    parser.add_argument(
        "--screen",
        choices=["left", "right", "all"],
        default="all",
        help="Screen region to capture (interval mode only)"
    )
    args = parser.parse_args()

    if args.mode == "interval":
        try:
            interval_main(screen=args.screen)
        except Exception as e:
            print(f"Error in interval mode: {e}")
            sys.exit(1)
    else:
        try:
            hotkey_main()
        except Exception as e:
            print(f"Error in hotkey mode: {e}")
            sys.exit(1)

if __name__ == "__main__":
    cli()
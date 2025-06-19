from PIL import ImageGrab
import pytesseract

def main():
    # Capture the whole screen
    image = ImageGrab.grab()
    # Recognize text
    text = pytesseract.image_to_string(image)
    print("Recognized text:")
    print(text)

if __name__ == "__main__":
    main()
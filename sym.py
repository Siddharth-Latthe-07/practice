import pytesseract
import cv2

# Set the path to the input image
img_path = 'maths.png'

# Load the input image and preprocess it
img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

# Set the configuration parameters for Tesseract
config = r'--psm 6 --oem 3 -c tessedit_char_whitelist=+-=()[]{}\/*%<>.,|'

# Run Tesseract on the preprocessed image
text = pytesseract.image_to_string(img, config=config)

# Print the recognized symbols
symbols = [s for s in text if s.isascii() and s.isprintable()]
print('Recognized symbols: ', symbols)

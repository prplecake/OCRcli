import gettext
import sys

from PIL import Image

import pyocr

try:
    input_image = sys.argv[1]
except IndexError:
    print('No input image provided. Exiting...')
    sys.exit(1)

tools = pyocr.get_available_tools()
if len(tools) == 0:
    print(gettext.gettext("No OCR tools found. Please install tesseract-ocr and/or libtesseract."))  # noqa: E501
    sys.exit(1)

tool = tools[0]
print(f'Using {tool.get_name()}')

langs = tool.get_available_languages()
langs.remove('osd')
lang = 'eng'

image = Image.open(input_image)

print(f'Input image: {input_image}\n\n')

out = tool.image_to_string(image, lang).replace("|", "I")

print(out)

import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np

# Load the image
image = cv2.imread('./test_samples/sample2/images/818.jpg')

# Convert the image to RGB (OpenCV uses BGR)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Convert the image to PIL format
pil_image = Image.fromarray(image)

# Load the font
font = ImageFont.truetype('uni.ttf', size=40, encoding='unic')

# Draw the text on the image
draw = ImageDraw.Draw(pil_image)
draw.text((10, 10), "हिन्दी टेक्स्ट", font=font, fill=(255, 0, 0))

# Convert the PIL image back to OpenCV format
cv2_image = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)

# Save the image
cv2.imwrite('output.jpg', cv2_image)
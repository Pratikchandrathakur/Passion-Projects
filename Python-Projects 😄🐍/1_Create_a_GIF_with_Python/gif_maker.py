import imageio.v3 as iio
from PIL import Image
import numpy as np

# List of image filenames
filenames = ['meme-1.png', 'meme-4.png']

# List to store resized images
images = []

# Open images, resize them to the same dimensions, convert to RGB, and append to the list
for filename in filenames:
    img = Image.open(filename)
    resized_img = img.resize((500, 500))  # Resize to 500x500 or desired dimensions
    rgb_img = resized_img.convert('RGB')  # Ensure all images are in RGB mode
    images.append(np.array(rgb_img))  # Convert the image to a NumPy array

# Save the images as a GIF
iio.imwrite('meme.gif', images, duration=500, loop=0)

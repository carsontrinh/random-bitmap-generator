from PIL import Image
from pyrandomdotorg.pyRandomdotOrg import *

SIZE_ROW = 127
SIZE_COLUMN = 127

user = ['name', 'email']
random = clientlib(user[0], user[1])

img = Image.new('RGB', (SIZE_ROW, SIZE_COLUMN), "white")  # Create a new white image
pixels = img.load()  # Create the pixel map

# Iterate through the pixels
for i in range(img.size[0]):
	
	"""
	Generate a column of RGB values. Originally, I wanted to request all of the values at the very
	beginning, but random.org didn't like that. The downside to this approach of requesting column
	by column is that it takes some time to generate the final image.
	"""

	rgb_values = random.IntegerGeneratorList(SIZE_COLUMN * 3, 0, 255)
	
	for j in range(img.size[1]):
		# Set the colors accordingly
		pixels[i,j] = (rgb_values[j * 3],\
                       rgb_values[j * 3 + 1],\
                       rgb_values[j * 3 + 2])

img.show()
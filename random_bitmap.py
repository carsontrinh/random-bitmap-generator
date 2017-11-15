from PIL import Image
from pyrandomdotorg.pyRandomdotOrg import *

SIZE_ROW = 128
SIZE_COLUMN = 128

user = ['name', 'email']
random = clientlib(user[0], user[1])

rgb_values = random.IntegerGeneratorList(SIZE_ROW * SIZE_COLUMN * 3, 0, 255)  # generate random integers


img = Image.new('RGB', (SIZE_ROW, SIZE_COLUMN), "white")  # create a new black image
pixels = img.load()  # create the pixel map


for i in range(img.size[0]):  # for every pixel:
    for j in range(img.size[1]):
        pixels[i,j] = (rgb_values[i * SIZE_ROW * 3 + j * 3],\
        			   rgb_values[i * SIZE_ROW * 3 + j * 3 + 1],\
        			   rgb_values[i * SIZE_ROW * 3 + j * 3] + 2) # set the colour accordingly

img.show()
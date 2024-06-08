
from PIL import Image

def colour(r,g,b):
    """"""
    # yellow
    if 150<r<235 and 75<g>150 and b<30:
        return "yellow"
    # green
    if 20<r<75 and g<255 and 5<b<90:
        return "green"
    # other
    else:
        return "other"
   
# -----------main-------#

#load an image of jellybeans
file = Image.open("jelly_beans.jpg")
jb_image = file.load()

#create an image output
test_image = Image.open("jelly_beans.jpg")

# list to store yellow pixels
yellow_pixels = []
green_pixels = []

# get size of image
width = file.width
height = file.height

# go through each pixel in the image
for x in range(width):
    for y in range(height):
        pixel_r = jb_image[x,y][0]
        pixel_g = jb_image[x,y][1]
        pixel_b = jb_image[x,y][2]

        # if its yellow, then add that pixel to the yellow list
        if colour(pixel_r, pixel_g, pixel_b) == "yellow":
            yellow_pixels.append(jb_image[x,y])
            white_out = (255,255,255)
            xy = (x,y)
            test_image.putpixel(xy, white_out)


# get number of yellow pixels
num_yellow = len(yellow_pixels)

# calculate the percentage of yellow pixels
total_pixels = width * height
yellow_ratio = num_yellow/total_pixels

# output a report
yellow_percent = yellow_ratio * 100
report = "there are {:.2f}% yellow jellybeans.".format(yellow_percent)
print(report)

# go through each pixel in the image
for x in range(width):
    for y in range(height):
        pixel_r = jb_image[x,y][0]
        pixel_g = jb_image[x,y][1]
        pixel_b = jb_image[x,y][2]

        # if its yellow, then add that pixel to the yellow list
        if colour(pixel_r, pixel_g, pixel_b) == "green":
            yellow_pixels.append(jb_image[x,y])
            white_out = (255,255,255)
            xy = (x,y)
            test_image.putpixel(xy, white_out)


# get number of yellow pixels
num_green = len(green_pixels)

# calculate the percentage of yellow pixels
total_pixels = width * height
green_ratio = num_yellow/total_pixels

# output a report
green_percent = green_ratio * 100
report = "there are {:.2f}% green jellybeans.".format(green_percent)
print(report)

test_image.save("test_image.jpg", "jpeg")
test_image.show()

from PIL import Image
import time

def colour(r, g, b):
    """Determines the colour based on RGB values."""
    # yellow
    if 150 < r < 235 and 75 < g < 150 and b < 30:
        return "yellow"
    # green
    if 20 < r < 75 and 5 < g < 255 and 5 < b < 90:
        return "green"
    # purple
    if 75 < r < 150 and 0 < g < 75 and 100 < b < 255:
        return "purple"
    # red
    if 150 < r < 255 and g < 75 and b < 75:
        return "red"
    # other    
    else:
        return "other"
# -----------main-------#

start_time = time.time() # current time

#load an image of jellybeans 
file = Image.open("jelly_beans.jpg")
jb_image = file.load()

load_time = time.time()

#create an image output
test_image = Image.open("jelly_beans.jpg")

# list to store yellow pixels 
yellow_pixels = []
green_pixels = []
red_pixels = []
purple_pixels = []


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

# go through each pixel in the image 
for x in range(width):
    for y in range(height):
        pixel_r = jb_image[x,y][0]
        pixel_g = jb_image[x,y][1]
        pixel_b = jb_image[x,y][2]

        # if its yellow, then add that pixel to the yellow list
        if colour(pixel_r, pixel_g, pixel_b) == "red":
            yellow_pixels.append(jb_image[x,y])
            white_out = (255,255,255)
            xy = (x,y)
            test_image.putpixel(xy, white_out)


# get number of yellow pixels 
num_red = len(red_pixels)

# calculate the percentage of yellow pixels
total_pixels = width * height
red_ratio = num_red/total_pixels

# output a report 
red_percent = red_ratio * 100
report = "there are {:.2f}% red jellybeans.".format(red_percent)
print(report)

# go through each pixel in the image 
for x in range(width):
    for y in range(height):
        pixel_r = jb_image[x,y][0]
        pixel_g = jb_image[x,y][1]
        pixel_b = jb_image[x,y][2]

        # if its yellow, then add that pixel to the yellow list
        if colour(pixel_r, pixel_g, pixel_b) == "purple":
            yellow_pixels.append(jb_image[x,y])
            white_out = (255,255,255)
            xy = (x,y)
            test_image.putpixel(xy, white_out)


# get number of yellow pixels 
num_purple = len(yellow_pixels)

# calculate the percentage of yellow pixels
total_pixels = width * height
purple_ratio = num_purple/total_pixels

# output a report 
purple_percent = purple_ratio * 100
report = "there are {:.2f}% purple jellybeans.".format(purple_percent)
print(report)

end_time = time.time()
image_load_time = load_time-start_time
elapsed_analysis_time = end_time-load_time
efficiency = "it took {:2f}s to load the image and creates the image objects .\n\
    the image analysis took {:2f}s to run.".format(image_load_time,
                                                   elapsed_analysis_time)

print(efficiency)

test_image.save("test_image.jpg", "jpeg")
test_image.show()
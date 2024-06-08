from PIL import Image
import time
import Image_Analysis

# -----------main-------#

#load an image of jellybeans 
file = Image.open("jelly_beans.jpg")
jb_image = file.load()

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

White_Out(jb_image,test_image,width,height , "yellow")


# get number of yellow pixels 
num_yellow = len(yellow_pixels)

# calculate the percentage of yellow pixels
total_pixels = width * height
yellow_ratio = num_yellow/total_pixels

# output a report 
yellow_percent = yellow_ratio * 100
report = "there are {:.2f}% yellow jellybeans.".format(yellow_percent)
print(report)


White_Out(jb_image,width,height , "green")


# get number of yellow pixels 
num_green = len(green_pixels)

# calculate the percentage of yellow pixels
total_pixels = width * height
green_ratio = num_yellow/total_pixels

# output a report 
green_percent = green_ratio * 100
report = "there are {:.2f}% green jellybeans.".format(green_percent)
print(report)


White_Out(jb_image,width,height , "red")


# get number of yellow pixels 
num_red = len(red_pixels)

# calculate the percentage of yellow pixels
total_pixels = width * height
red_ratio = num_red/total_pixels

# output a report 
red_percent = red_ratio * 100
report = "there are {:.2f}% red jellybeans.".format(red_percent)
print(report)


White_Out(jb_image,width,height , "purple")


# get number of yellow pixels 
num_purple = len(yellow_pixels)

# calculate the percentage of yellow pixels
total_pixels = width * height
purple_ratio = num_purple/total_pixels

# output a report 
purple_percent = purple_ratio * 100
report = "there are {:.2f}% purple jellybeans.".format(purple_percent)
print(report)

test_image.save("test_image.jpg", "jpeg")
test_image.show()


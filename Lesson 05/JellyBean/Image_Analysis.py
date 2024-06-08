from PIL import Image

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
    
def White_Out(imgFile ,test_image,width , height, fromColor):
    yellow_pixels = []
    # go through each pixel in the image 
    for x in range(width):
        for y in range(height):
            pixel_r = imgFile[x,y][0]
            pixel_g = imgFile[x,y][1]
            pixel_b = imgFile[x,y][2]

            # if its yellow, then add that pixel to the yellow list
            if colour(pixel_r, pixel_g, pixel_b) == fromColor:
                yellow_pixels.append(imgFile[x,y])
                white_out = (255,255,255)
                xy = (x,y)
                test_image.putpixel(xy, white_out)
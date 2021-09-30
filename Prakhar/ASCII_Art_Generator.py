# Pillow library
import PIL.Image

# 256 is divided into 11 equal parts forming a group of 25 each. Now intensities lying in
# each group will be replaced by a specific character. (0-25) with @
ASCII_CHAR = ["@","#","S","%","?","*","+",";",":",",","."]

# To resize the image taking into consideration the correct ratio of W and H


def resize_img(image, new_width):
    width, height = image.size
    ratio = height/width
    new_height = int((new_width*ratio)/2) # adjustment using trial
    resized_img = image.resize((new_width,new_height))
    return resized_img

# To convert image from RGB to Grayscale


def grayify(image):
    grayscale_image = image.convert("L")
    print(grayscale_image)
    return grayscale_image

# To assign character to each pixel according to their group in which they lie


def pixel_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHAR[pixel//25] for pixel in pixels])
    return characters


def main():
    path = input("Enter image Path")
    new_width = int(input("Input required width"))
    try:
        image = PIL.Image.open(path)
    except:
        print("Invalid path")
    new_image_data = pixel_to_ascii(grayify(resize_img(image, new_width)))
    pixel_count = len(new_image_data)
    print(pixel_count)
    ascii_image = "\n".join(new_image_data[i:(i+new_width)] for i in range(0, pixel_count, new_width))

    with open("ascii_image.txt", "w") as f:
        f.write(ascii_image)


main()

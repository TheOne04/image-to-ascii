from PIL import Image

def pixel_to_ascii(pixel):
    # TODO: If image not in RGB format try to convert else show error message
    
    brightness = (max(pixel) + min(pixel)) / 2

    chars = '              `^",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'

    num = 255 / (len(chars) - 1)

    return chars[round(brightness / num)]


def resize(image):
    W = 100


    r = image.size[1] / image.size[0]
    H = int(W * r * 0.5)

    image = image.resize((W, H), Image.LANCZOS)
    return image

def convert_to_ascii(image):
    image = resize(image)
    ascii_art = ""
    # TODO: decide whether to hardcode dimensions
    width, height = image.size

    pixels = list(image.getdata())

    for i in range(height):
        for j in range(width):
            # Index Pixel
            index = i * width + j
            
            # Calculate ascii character
            ascii_art += pixel_to_ascii(pixels[index])
            
            # Store into string

        # Add newline to string
        ascii_art += "\n"

    return ascii_art
 


if __name__ == "__main__":
    image = Image.open(input("Enter path to image: "))

    print(convert_to_ascii(image))

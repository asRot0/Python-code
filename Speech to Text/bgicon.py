from PIL import Image


def remove_background(image_path, threshold):
    # Open the image
    image = Image.open(image_path).convert("RGBA")

    # Get the pixel data of the image
    pixels = image.getdata()

    # Create a new transparent image
    transparent_image = Image.new("RGBA", image.size, (0, 0, 0, 0))
    transparent_pixels = []

    # Iterate over the pixels and apply the threshold
    for pixel in pixels:
        if pixel[3] > threshold:
            transparent_pixels.append((pixel[0], pixel[1], pixel[2], 255))
        else:
            transparent_pixels.append((0, 0, 0, 0))

    # Update the pixel data of the transparent image
    transparent_image.putdata(transparent_pixels)

    return transparent_image


# Specify the path to the input image
input_image_path = "input_image.png"

# Specify the threshold value (adjust as needed)
threshold = 128

# Remove the background and get the resulting image
output_image = remove_background(input_image_path, threshold)

# Save the resulting image
output_image_path = "output_image.png"
output_image.save(output_image_path)

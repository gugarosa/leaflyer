import argparse

from PIL import Image

def get_arguments():
    """Gets arguments from the command line.

    Returns:
        A parser with the input arguments.

    """

    parser = argparse.ArgumentParser(usage='Pixelates an individual image.')

    parser.add_argument('input_image', help='Input image file', type=str)

    return parser.parse_args()

if __name__ == '__main__':
    # Gathers the input arguments and its variables
    args = get_arguments()
    input_image = args.input_image

    # Defines the amount of pixels to be used and their category
    pixel_size = [1, 5, 10, 25, 50]
    pixel_category = ['common', 'uncommon', 'rare', 'epic', 'legendary']

    # Defines a list to hold the gif images
    gif = []

    # Iterates through every possibility
    for p_s, p_c in zip(pixel_size, pixel_category):
        # Opens the image with Pillow
        im = Image.open(input_image)

        # Performs the downscaling
        width, height = int(im.size[0] / p_s), int(im.size[1] / p_s)
        im = im.resize((width, height), Image.NEAREST)

        # Performs the upscaling
        width, height = int(im.size[0] * p_s), int(im.size[1] * p_s)
        im = im.resize((width, height), Image.NEAREST)

        # Saves the output image
        im.save(f'{p_c}_{input_image}')

        # Appends the image to the `gif` list
        gif.append(im)

    # Outputs the gif as well
    gif[0].save(f'{input_image}.gif', save_all=True, append_images=gif[1:] + gif[::-1], duration=100, loop=0)

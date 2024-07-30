from PIL import Image
import os

# Constants for the script
DESIRED_WIDTH = 1560
DESIRED_HEIGHT = 960
TRIM_FROM = 'top-left'  # Options: 'top', 'bottom', 'left', 'right', 'top-left', etc.
SUPPORTED_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.gif']

def find_first_image(directory):
    """
    Finds the first image file in the specified directory.

    Args:
        directory (str): The directory to search for images.

    Returns:
        str: The full path to the first found image file, or None if no image is found.
    """
    for filename in os.listdir(directory):
        if any(filename.lower().endswith(ext) for ext in SUPPORTED_EXTENSIONS):
            return os.path.join(directory, filename)
    return None

def trim_image(input_image_path, output_image_path, desired_width, desired_height, trim_from):
    """
    Trims an image to the specified dimensions.

    Args:
        input_image_path (str): The path to the input image file.
        output_image_path (str): The path to save the trimmed image.
        desired_width (int): The desired width of the trimmed image.
        desired_height (int): The desired height of the trimmed image.
        trim_from (str): The direction from which to trim the image.
    """
    try:
        with Image.open(input_image_path) as img:
            width, height = img.size

            # Determine crop coordinates
            left, top, right, bottom = 0, 0, width, height

            if 'left' in trim_from:
                left = 0
                right = desired_width
            elif 'right' in trim_from:
                left = width - desired_width
                right = width
            else:
                left = (width - desired_width) / 2
                right = (width + desired_width) / 2

            if 'top' in trim_from:
                top = 0
                bottom = desired_height
            elif 'bottom' in trim_from:
                top = height - desired_height
                bottom = height
            else:
                top = (height - desired_height) / 2
                bottom = (height + desired_height) / 2

            cropped_img = img.crop((left, top, right, bottom))
            cropped_img.save(output_image_path)
            print(f"Image has been trimmed to {desired_width}x{desired_height} from {trim_from} and saved as '{output_image_path}'")
    except Exception as e:
        print(f"Error processing image: {e}")

if __name__ == "__main__":
    script_directory = os.path.dirname(os.path.abspath(__file__))
    input_image_path = find_first_image(script_directory)

    if input_image_path:
        output_image_path = os.path.join(script_directory, 'Trimmed.png')
        trim_image(input_image_path, output_image_path, DESIRED_WIDTH, DESIRED_HEIGHT, TRIM_FROM)
    else:
        print("No image file found in the directory.")

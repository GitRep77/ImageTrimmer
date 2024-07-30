from PIL import Image
import os

# Variables to specify desired width, height, and trim direction
desired_width = 1560
desired_height = 960
trim_from = 'top-left'  # Change this to 'top', 'bottom', 'left', 'right', 'top-left', etc.

def find_first_image(directory):
    # Supported image file extensions
    supported_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.gif']
    for filename in os.listdir(directory):
        if any(filename.lower().endswith(ext) for ext in supported_extensions):
            return os.path.join(directory, filename)
    return None

def trim_image(input_image_path, output_image_path, desired_width, desired_height, trim_from):
    # Open the image file
    with Image.open(input_image_path) as img:
        # Get the current dimensions of the image
        width, height = img.size
        
        # Calculate the coordinates to crop the image
        left, top, right, bottom = 0, 0, width, height
        
        if 'left' in trim_from:
            left = 0
            right = desired_width
        elif 'right' in trim_from:
            left = width - desired_width
            right = width
        else:  # center horizontally
            left = (width - desired_width) / 2
            right = (width + desired_width) / 2
        
        if 'top' in trim_from:
            top = 0
            bottom = desired_height
        elif 'bottom' in trim_from:
            top = height - desired_height
            bottom = height
        else:  # center vertically
            top = (height - desired_height) / 2
            bottom = (height + desired_height) / 2
        
        # Crop the image
        cropped_img = img.crop((left, top, right, bottom))
        
        # Save the cropped image to the output path
        cropped_img.save(output_image_path)

# Directory where the script is located
script_directory = os.path.dirname(os.path.abspath(__file__))

# Find the first image in the script directory
input_image_path = find_first_image(script_directory)

if input_image_path:
    # Path for the output image
    output_image_path = os.path.join(script_directory, 'Trimmed.png')
    
    # Call the function to trim the image
    trim_image(input_image_path, output_image_path, desired_width, desired_height, trim_from)
    
    print(f"Image has been trimmed to {desired_width}x{desired_height} from {trim_from} and saved as 'Trimmed.png'")
else:
    print("No image file found in the directory.")

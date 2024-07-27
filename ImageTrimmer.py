from PIL import Image
import os

def find_first_image(directory):
    # Supported image file extensions
    supported_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.gif']
    for filename in os.listdir(directory):
        if any(filename.lower().endswith(ext) for ext in supported_extensions):
            return os.path.join(directory, filename)
    return None

def trim_image(input_image_path, output_image_path, desired_width, desired_height):
    # Open the image file
    with Image.open(input_image_path) as img:
        # Get the current dimensions of the image
        width, height = img.size
        
        # Calculate the coordinates to crop the image
        left = (width - desired_width) / 2
        top = (height - desired_height) / 2
        right = (width + desired_width) / 2
        bottom = (height + desired_height) / 2
        
        # Crop the image
        cropped_img = img.crop((left, top, right, bottom))
        
        # Save the cropped image to the output path
        cropped_img.save(output_image_path)

# Variables to specify desired width and height
desired_width = 1560
desired_height = 960

# Directory where the script is located
script_directory = os.path.dirname(os.path.abspath(__file__))

# Find the first image in the script directory
input_image_path = find_first_image(script_directory)

if input_image_path:
    # Path for the output image
    output_image_path = os.path.join(script_directory, 'Trimmed.png')
    
    # Call the function to trim the image
    trim_image(input_image_path, output_image_path, desired_width, desired_height)
    
    print(f"Image has been trimmed to {desired_width}x{desired_height} and saved as 'Trimmed.png'")
else:
    print("No image file found in the directory.")

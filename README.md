
# Image Trimmer

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-blue)


# Image Trimmer

## Overview

Image Trimmer is a simple yet precise Python script designed to trim the edges of an image to specified dimensions. It automatically detects the first image in the directory where the script is stored, crops it to the desired size, and saves the output as "Trimmed.png". This tool is ideal for those needing quick and accurate image resizing.

## Features

- Automatically finds the first image in the script's directory.
- Trims the image to user-defined dimensions.
- Outputs the trimmed image as "Trimmed.png".
- Easy to use, even for those with minimal Python experience.

## Requirements

- Python 3.x
- Pillow library (Python Imaging Library)

## Installation

1. **Python**: Ensure you have Python 3.x installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

2. **Pillow**: Install the Pillow library using pip. Open your terminal or command prompt and run:
   ```sh
   pip install pillow
   ```

## Usage

### Step 1: Clone the Repository

Clone the repository from GitHub to your local machine using the following command:
```sh
git clone https://github.com/yourusername/imagetrimmer.git
```
Navigate to the cloned directory:
```sh
cd imagetrimmer
```

### Step 2: Place Your Image

Place the image you want to trim in the same directory as the script. Ensure there is only one image in the directory, as the script will automatically detect and process the first image it finds.

### Step 3: Adjust the Desired Dimensions

Open the `trim_image.py` script in your preferred text editor. Modify the `desired_width` and `desired_height` variables to the dimensions you want:
```python
# Variables to specify desired width and height
desired_width = 1560
desired_height = 960
```

### Step 4: Run the Script

Run the script using the terminal or command prompt:
```sh
python trim_image.py
```

The script will process the image, trim it to the specified dimensions, and save the output as `Trimmed.png` in the same directory.

### Example

Before running the script, your directory should look like this:
```
imagetrimmer/
├── trim_image.py
└── input_image.jpg
```

After running the script, it will look like this:
```
imagetrimmer/
├── trim_image.py
├── input_image.jpg
└── Trimmed.png
```

## Support

If you encounter any issues or have questions, please open an issue on the [GitHub repository](https://github.com/yourusername/imagetrimmer/issues).

## Contributing

We welcome contributions! Please read our [contributing guidelines](CONTRIBUTING.md) for more details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## Overview

Image Trimmer is a simple yet precise Python script designed to trim the edges of an image to specified dimensions. It automatically detects the first image in the directory where the script is stored, crops it to the desired size, and saves the output as "Trimmed.png". This tool is ideal for those needing quick and accurate image resizing.

## Features

- Automatically finds the first image in the script's directory.
- Trims the image to user-defined dimensions.
- Outputs the trimmed image as "Trimmed.png".
- Easy to use, even for those with minimal Python experience.

## Requirements

- Python 3.x
- Pillow library (Python Imaging Library)

## Installation

1. **Python**: Ensure you have Python 3.x installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

2. **Pillow**: Install the Pillow library using pip. Open your terminal or command prompt and run:
   ```sh
   pip install pillow
   ```

## Usage

### Step 1: Clone the Repository

Clone the repository from GitHub to your local machine using the following command:
```sh
git clone https://github.com/yourusername/imagetrimmer.git
```
Navigate to the cloned directory:
```sh
cd imagetrimmer
```

### Step 2: Place Your Image

Place the image you want to trim in the same directory as the script. Ensure there is only one image in the directory, as the script will automatically detect and process the first image it finds.

### Step 3: Adjust the Desired Dimensions

Open the `trim_image.py` script in your preferred text editor. Modify the `desired_width` and `desired_height` variables to the dimensions you want:
```python
# Variables to specify desired width and height
desired_width = 1560
desired_height = 960
```

### Step 4: Run the Script

Run the script using the terminal or command prompt:
```sh
python trim_image.py
```

The script will process the image, trim it to the specified dimensions, and save the output as `Trimmed.png` in the same directory.

### Example

Before running the script, your directory should look like this:
```
imagetrimmer/
├── trim_image.py
└── input_image.jpg
```

After running the script, it will look like this:
```
imagetrimmer/
├── trim_image.py
├── input_image.jpg
└── Trimmed.png
```

## Support

If you encounter any issues or have questions, please open an issue on the [GitHub repository](https://github.com/yourusername/imagetrimmer/issues).

## Contributing

We welcome contributions! Please read our [contributing guidelines](CONTRIBUTING.md) for more details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

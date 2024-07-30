
# Image Trimmer

![Build Status](https://img.shields.io/badge/build-passing-brightgreen) ![Python Version](https://img.shields.io/badge/python-3.8%2B-blue) ![License](https://img.shields.io/badge/license-MIT-blue)

## Overview

Image Trimmer is a simple yet precise Python script designed to trim the edges of an image to specified dimensions. It automatically detects the first image in the directory where the script is stored, crops it to the desired size, and saves the output as "Trimmed.png". This tool is ideal for quick and accurate image resizing.

## Features

- **Automatic Detection:** Finds the first image in the script's directory.
- **Custom Dimensions:** Trims the image to user-defined dimensions with options for trimming direction (e.g., top, bottom, left, right, or combinations).
- **Output:** Saves the trimmed image as "Trimmed.png".
- **User-Friendly:** Easy to use, even for those with minimal Python experience.

## Requirements

- Python 3.x
- Pillow library (Python Imaging Library)

## Installation

1. **Python:** Ensure Python 3.x is installed. [Download here](https://www.python.org/downloads/).

2. **Dependencies:** Install the required Python packages using `requirements.txt`:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

### Step 1: Clone the Repository

Clone the repository and navigate to the directory:
```sh
git clone https://github.com/yourusername/imagetrimmer.git
cd imagetrimmer
```

### Step 2: Install Dependencies

Ensure all necessary packages are installed:
```sh
pip install -r requirements.txt
```

### Step 3: Place Your Image

Place the image to be trimmed in the same directory as the script. The script processes the first image it finds.

### Step 4: Adjust the Desired Dimensions

Edit the `trim_image.py` script:
```python
# Specify desired dimensions
desired_width = 1560
desired_height = 960
trim_from = 'top-left'  # Options: 'top', 'bottom', 'left', 'right', 'top-left', etc.
```

### Step 5: Run the Script

Execute the script:
```sh
python trim_image.py
```

This will generate a `Trimmed.png` file with the specified dimensions.

## Support

For issues or questions, open an issue on the [GitHub repository](https://github.com/yourusername/imagetrimmer/issues).

## Contributing

We welcome contributions! Please read our [contributing guidelines](CONTRIBUTING.md) for more details.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

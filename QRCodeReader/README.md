# QRCodeReader

QRCodeReader is a Python script that utilizes OpenCV and PyZbar to scan images for QR codes and display the decoded data.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Limitations](#limitations)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This Python script provides a simple yet powerful tool for scanning images to detect and decode QR codes. The script uses the OpenCV library for image processing and the PyZbar library for QR code decoding.

## Features

- Scan images for QR codes.
- Display the decoded data on the image.
- Support for multiple images in a batch.

## Limitations

PyZbar, the library used for QR code decoding, has some limitations that you should be aware of:

- **Barcode Types:** Primarily focuses on 1D and 2D barcodes; may lack support for specialized formats.

- **3D Barcode Support:** Limited or nonexistent support for reading 3D barcodes.

Feel free to customize the `image_list` variable with the paths to your specific images.

## Installation

1. Clone the repository:

   ```bash
    git clone https://github.com/adil6572/small-opencv-project.git
    cd small-opencv-project/QRCodeReader
   ```


2. Install the required dependencies:

   ```bash
   pip install opencv-python pyzbar
   ```

## Usage

To utilize the QRCodeReader script, follow these steps:

1. Open the `QRCodeReader.py` file.
2. Modify the `image_list` variable by adding the paths to your desired images. For example:

   ```python
   image_list = ["./your_image1.jpg", "./your_image2.png", "./your_image3.png", "./your_image4.jpg", "./your_image5.jpg", "./your_image6.jpeg"]
   ```

3. Save the changes to the file.

4. Open your terminal or command prompt.

5. Run the Python script:

   ```bash
   python QRCodeReader.py
   ```

6. The script will display the images with detected QR codes, and the decoded data will be printed in the console.

Feel free to customize the `image_list` variable with the paths to your specific images.

## Contributing

Contributions to the QRCodeReader project are welcome! If you have ideas for improvements, additional features, or bug fixes, please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with clear messages.
4. Push your changes to your fork.
5. Open a pull request with a detailed description of your changes.

## License

This project is licensed under the MIT License.

Feel free to reach out if you have any questions or suggestions! Happy scanning! 🚀📷


# 📸 Image Corner Rounding Script 🌐

This is a Python script that allows you to round the corners of an image.

## 🔧 Installation

Before running the script, make sure to install the necessary Python libraries. You can install these using pip:

```bash
pip install pillow
```
## 🚀 Usage

The script is used from the command line and takes three arguments:

1. `image_path`: The path to the input image.
2. `output_path`: The path where the rounded image should be saved.
3. `radius`: The radius for the rounded corners.

You can use the script like this:

```bash
python round_corners.py input.png output.png 50
```

This will create a new image file called `output.png` with rounded corners of radius 50 pixels.

## 📖 Help

For more information on how to use the script, you can ask for help:

```bash
python round_corners.py --help
```

This will print a helpful message explaining how to use the script.

## 💡 Note

The script expects the image to be in a format that supports transparency (like PNG). If the image is in a different format (like JPG), the script will still run, but the corners outside the rounded area will be black.

Enjoy your image processing! 🎉

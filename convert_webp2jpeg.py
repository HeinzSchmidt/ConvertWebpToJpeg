import sys
import os
from PIL import Image

def webp_to_jpeg(input_path):
    # Get the directory and filename without extension
    directory, filename = os.path.split(input_path)
    filename_without_ext, _ = os.path.splitext(filename)
    
    # Create the output path
    output_path = os.path.join(directory, filename_without_ext + ".jpg")

    # Open the WebP image
    image = Image.open(input_path)

    # Convert image to RGB mode (JPEG doesn't support alpha channel)
    if image.mode == "RGBA":
        image = image.convert("RGB")

    # Save the image as JPEG
    image.save(output_path, "JPEG")
    print(f"Image converted successfully: {output_path}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_webp_file>")
        sys.exit(1)

    input_image = sys.argv[1]
    if not input_image.lower().endswith(".webp"):
        print("Error: Input file must be a WebP image.")
        sys.exit(1)

    webp_to_jpeg(input_image)

if __name__ == "__main__":
    main()

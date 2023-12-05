import os
from PIL import Image

def resize_image(image_path, output_path, target_size=(640, 640)):
    original_image = Image.open(image_path)
    resized_image = original_image.resize(target_size, Image.LANCZOS)
    resized_image.save(output_path)

def resize_images_in_directory(directory_path, output_directory, target_size=(640, 640)):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Process each image in the directory
    for filename in os.listdir(directory_path):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            input_image_path = os.path.join(directory_path, filename)
            output_image_path = os.path.join(output_directory, filename)

            resize_image(input_image_path, output_image_path, target_size)

if __name__ == "__main__":
    input_directory = "images"
    output_directory = "images"
    target_size = (640, 640)

    resize_images_in_directory(input_directory, output_directory, target_size)

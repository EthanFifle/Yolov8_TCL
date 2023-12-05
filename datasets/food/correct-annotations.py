import os
from PIL import Image

def normalize_coordinates(x_min, y_min, x_max, y_max, original_width, original_height):
    # Calculate center coordinates, width, and height
    center_x = (x_min + x_max) / 2
    center_y = (y_min + y_max) / 2
    box_width = x_max - x_min
    box_height = y_max - y_min

    # Calculate scale factors
    scale_x = 640 / original_width
    scale_y = 640 / original_height

    # Scale normalized coordinates based on the new dimensions (640 by 640)
    normalized_center_x = (center_x * scale_x) / 640
    normalized_center_y = (center_y * scale_y) / 640
    normalized_width = (box_width * scale_x) / 640
    normalized_height = (box_height * scale_y) / 640

    return normalized_center_x, normalized_center_y, normalized_width, normalized_height

def process_annotations_file(file_path, output_path, image_width, image_height):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(output_path, 'w') as output_file:
        for line in lines:
            # Strip the newline character
            line = line.strip()

            # Split the line into tokens
            tokens = line.split()

            # Check if the line is not empty and starts with 'Food'
            if tokens and tokens[0] == 'Food':
                # Change 'Food' to '18'
                tokens[0] = '18'

                # Process each bounding box individually
                for i in range(1, len(tokens), 4):
                    # Normalize bounding box coordinates
                    x_min, y_min, x_max, y_max = map(float, tokens[i:i+4])
                    normalized_center_x, normalized_center_y, normalized_width, normalized_height = \
                        normalize_coordinates(x_min, y_min, x_max, y_max, image_width, image_height)

                    # Create a new line for each bounding box
                    modified_line = ' '.join([tokens[0]] + [f'{coord:.6f}' for coord in 
                                                      [normalized_center_x, normalized_center_y, normalized_width, normalized_height]])
                    
                    # Write the modified line directly to the output file
                    output_file.write(modified_line + '\n')

            else:
                # If the line doesn't start with 'Food', write it unchanged to the output file
                output_file.write(line + '\n')


def get_image_dimensions(image_path):
    with Image.open(image_path) as img:
        width, height = img.size
    return width, height

if __name__ == "__main__":
    input_directory = "labels"
    output_directory = "labels"
    
    # Create output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Process each annotation file in the directory
    for filename in os.listdir(input_directory):
        if filename.endswith('.txt'):
            input_file_path = os.path.join(input_directory, filename)
            output_file_path = os.path.join(output_directory, filename)

            # Construct the corresponding image path
            image_name = os.path.splitext(filename)[0] + '.jpg'
            image_path = os.path.join("/Users/naman/downloads/Food", image_name)

            # Get image dimensions
            image_width, image_height = get_image_dimensions(image_path)

            # Process the annotation file
            process_annotations_file(input_file_path, output_file_path, image_width, image_height)

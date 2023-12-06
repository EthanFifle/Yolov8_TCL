# Created by Ethan
import os
import shutil
import random

# 240 for 8% of images for validate set
# use num_images_to_move=None to move all images in a directory


def move_images(source_folder, destination_folder, num_images_to_move, log_file):

    # Check if source_folder is empty
    if not os.listdir(source_folder):
        raise ValueError("Source folder is empty. There are no images to move.")

    # Get a list of all files in the source folder
    all_files = os.listdir(source_folder)

    # Filter only image files (you may need to adjust the file extensions)
    image_files = [file for file in all_files if file.lower().endswith(('.png', '.jpg', '.jpeg'))]

    # Use all images if num_images_to_move is not specified
    if num_images_to_move is None:
        selected_files = image_files
    else:
        # Shuffle the image files to randomly select the specified number
        random.shuffle(image_files)
        selected_files = image_files[:num_images_to_move]

    # Ensure the destination folder exists
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Move the selected files to the destination folder and write their names to the log file
    moved_count = 0
    with open(log_file, 'a') as log:
        for file in selected_files:
            source_path = os.path.join(source_folder, file)
            destination_path = os.path.join(destination_folder, file)
            shutil.move(source_path, destination_path)
            log.write(f"{file}\n")
            moved_count += 1
            print(f"Moved: {file}")

    print(f"Total files moved: {moved_count}")


if __name__ == "__main__":
    # Replace these paths with your actual source and destination folder paths
    source_folder_path = "train/images"
    destination_folder_path = "valid/images"

    # Replace this with your desired log file path
    log_file_path = "moved_valid_images.txt"

    # ******** REMEMBER TO UPDATE num_images_to_move=None (or #) before running!!!! ********** #

    move_images(source_folder_path, destination_folder_path, 120, log_file=log_file_path)

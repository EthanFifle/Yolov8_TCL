import os
import shutil


def move_images(log_file, source_folder, destination_folder, moved_images_file):
    # Ensure the source and destination image folders exist
    if not os.path.exists(source_folder):
        print(f"Error: Source folder '{source_folder}' does not exist.")
        return

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Read the names of moved images from the log file
    moved_images = []
    with open(log_file, 'r') as log:
        moved_images = [line.strip() for line in log.readlines()]

    moved_count = 0
    # Move corresponding image files to the destination folder and log their names
    with open(moved_images_file, 'a') as moved_images_log:
        for image_name in moved_images:
            source_image_path = os.path.join(source_folder, image_name)
            destination_image_path = os.path.join(destination_folder, image_name)

            if os.path.exists(source_image_path):
                shutil.move(source_image_path, destination_image_path)
                moved_images_log.write(f"{image_name}\n")
                moved_count += 1
                print(f"Moved: {image_name}")
            else:
                print(f"Warning: Image not found with name {image_name}")

    print(f"Total files moved: {moved_count}")

    if os.path.getsize(moved_images_file) > 0:
        print(f"Overwriting {moved_images_file}")
        with open(moved_images_file, 'w') as moved_labels_log:
            for image_name in moved_images:
                label_file_name = os.path.splitext(image_name)[0] + ".txt"
                moved_labels_log.write(f"{label_file_name}\n")

if __name__ == "__main__":
    # Replace these paths with your actual source and destination image folder paths
    source_image_folder_path = "taco/train/images"
    destination_image_folder_path = "food/train/images"

    # Replace this with your desired log file path
    moved_images_file_path = "moved_train_images.txt"

    move_images(log_file="moved_train_images.txt", source_folder=source_image_folder_path, destination_folder=destination_image_folder_path, moved_images_file=moved_images_file_path)

import os
import shutil


def move_labels(log_file="moved_images.txt", source_folder="source_labels", destination_folder="destination_labels", moved_labels_file="moved_labels.txt"):
    # Ensure the source and destination label folders exist
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
    # Mdove corresponding label files to the destination folder and log their names
    with open(moved_labels_file, 'a') as moved_labels_log:
        for image_name in moved_images:
            label_file_name = os.path.splitext(image_name)[0] + ".txt"
            source_label_path = os.path.join(source_folder, label_file_name)
            destination_label_path = os.path.join(destination_folder, label_file_name)

            if os.path.exists(source_label_path):
                shutil.move(source_label_path, destination_label_path)
                moved_labels_log.write(f"{label_file_name}\n")
                moved_count += 1
                print(f"Moved: {label_file_name}")
            else:
                print(f"Warning: Label file not found for image {image_name}")

    print(f"Total files moved: {moved_count}")

if __name__ == "__main__":
    # Replace these paths with your actual source and destination label folder paths
    source_label_folder_path = "Food/train/labels"
    destination_label_folder_path = "taco/train/labels"

    # Replace this with your desired log file path
    moved_labels_file_path = "moved_labels.txt"

    move_labels(log_file="moved_images.txt", source_folder=source_label_folder_path, destination_folder=destination_label_folder_path, moved_labels_file=moved_labels_file_path)

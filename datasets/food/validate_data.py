# Created by Ethan
import os


def validate_move(log_file, moved_labels_file):
    # Read the names of moved images and labels from the log files
    with open(log_file, 'r') as log:
        moved_images = {line.strip() for line in log.readlines()}

    with open(moved_labels_file, 'r') as moved_labels_log:
        moved_labels = {line.strip() for line in moved_labels_log.readlines()}

    # Extract the names without extensions for comparison
    moved_images_names = {os.path.splitext(name)[0] for name in moved_images}
    moved_labels_names = {os.path.splitext(name)[0] for name in moved_labels}

    # Find the difference in names between moved_images and moved_labels
    images_not_in_labels = moved_images_names - moved_labels_names
    labels_not_in_images = moved_labels_names - moved_images_names

    # Print the results of the validation
    if not images_not_in_labels and not labels_not_in_images:
        print(f"Validation passed. Number of files in {log_file}: {len(moved_images)} | Number of files in {moved_labels_file}: {len(moved_labels)}")
    else:
        print("Validation failed. The following files are not matching:")
        if images_not_in_labels:
            print(f"Files in {log_file} but not in {moved_labels_file}:")
            for name in images_not_in_labels:
                print(f"{name}.jpg")
        if labels_not_in_images:
            print(f"Files in {moved_labels_file} but not in {log_file}:")
            for name in labels_not_in_images:
                print(f"{name}.txt")


if __name__ == "__main__":
    # Replace this with the actual paths to your moved_images.txt and moved_valid_labels.txt files
    moved_images_file_path = "moved_valid_images.txt"
    moved_labels_file_path = "moved_valid_labels.txt"

    validate_move(log_file=moved_images_file_path, moved_labels_file=moved_labels_file_path)

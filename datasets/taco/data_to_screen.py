# Created by Ethan
import os

folder_path = 'valid/labels'
class_id = 18  # Class id to look for

# Iterate through files in the folder
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    # Open the file and check each line
    with open(file_path, 'r') as file:
        # List to store lines that start with the specified class_id
        lines_with_class_id = []

        for line_number, line in enumerate(file, start=1):
            # Check if the line starts with the specified class_id
            if line.startswith(str(class_id)) and (len(line) == 1 or not line[len(str(class_id))].isdigit()):
                lines_with_class_id.append(f"Line {line_number}: {line.strip()}")

        # Print lines if any
        if lines_with_class_id:
            print(f"File: {filename} has class {class_id} in:")
            for line in lines_with_class_id:
                print(line)

print("Finished checking files.")
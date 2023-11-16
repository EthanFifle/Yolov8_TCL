import os

folder_path = 'train/labels'
class_id = 17  # Class id to look for

# Iterate through files in the folder
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    # Open the file and check each line
    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            # Check if the line starts with the specified class_id
            if line.startswith(str(class_id)) and (len(line) == 1 or not line[len(str(class_id))].isdigit()):
                print(f"File: {filename} has class {class_id} in")
                print(f"Line {line_number}: {line.strip()} ")

print("Finished checking files.")

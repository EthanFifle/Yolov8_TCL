import os

folder_path = 'datacleanup'
class_id = 1  # Class id to delete from all annotations

# Iterate through files in the folder
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    # Open the file and read all lines
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Filter out lines starting with the specified class_id
    filtered_lines = []
    for line in lines:
        # Check if the line starts with the specified class_id
        if not (line.startswith(str(class_id) + ' ') or line == str(class_id)):
            filtered_lines.append(line.strip())

    # Write the updated lines back to the file
    with open(file_path, 'w') as updated_file:
        updated_file.write('\n'.join(filtered_lines))

print("Finished updating files.")
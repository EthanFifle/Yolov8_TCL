import os

# Specify the folder path and class ids
folder_path = 'datacleanup'
current_class_id = 5
class_id_to_replace = 17


def replace_class_id(file_path, current_class_id, class_id_to_replace):
    # Open the file and read all lines
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Replace the specified class_id with the new class_id
    updated_lines = []
    for line in lines:
        if line.startswith(str(current_class_id) + ' '):
            # Replace the class_id if it appears at the beginning of the line
            updated_lines.append(line.replace(str(current_class_id), str(class_id_to_replace), 1).strip())
        elif line == str(current_class_id):
            # Replace the entire line if it matches the specified class_id
            updated_lines.append(str(class_id_to_replace))
        elif line.strip():  # Check if the line is not empty
            updated_lines.append(line.strip())

    # Write the updated lines back to the file
    with open(file_path, 'w') as updated_file:
        updated_file.write('\n'.join(updated_lines))


# Iterate through files in the folder and replace class_id with to_replace_class_id
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    replace_class_id(file_path, current_class_id, class_id_to_replace)

print("Finished updating files.")
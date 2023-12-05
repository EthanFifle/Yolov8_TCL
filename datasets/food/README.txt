correct-annotations.py - updates the annotations for the collected food labels
image_640.py - resizes the food images to 640x640 resolution for optimal compatibility
split_data.py - splits up food images at random to a destination of your choice (train/images or valid/images)
sort_data.py - brings the annotations (labels) for those images over to the desired destination (train/labels or valid/labels)
validate_data.py - validates that the transactions and movements of files occurred correctly
undo_img_changes.py - moves the images back to where they came from, effectively undoing spilt_data.py

All text files starting with "moved..." keep track of moved files so that undoing changes are simple
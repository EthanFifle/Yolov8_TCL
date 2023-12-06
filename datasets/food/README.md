
### Implemented Scripts for Data Pre-processing 

- `correct-annotations` - created to update the annotations for the collected food labels 
- `image_640` - created to resize the food images to 640x640 resolution for optimal compatibility
- `split_data` - created to split up food images at random to a destination of your choice (train/images or valid/images)
- `sort_data` - created to bring the annotations (labels) for those images over to the desired destination (train/labels or valid/labels)
- `validate_data` - created to validate that the transactions and movements of files occurred correctly
- `undo_img_changes` - created to move the images back to where they came from, effectively undoing spilt_data.py

All text files starting with `moved...` are created by the above scripts to keep track of moved files so that undoing changes are simple
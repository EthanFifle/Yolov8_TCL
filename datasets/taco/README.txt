In this folder is our final dataset used to train our model

Most recently it combines taco (which is an open source trash dataset, see also LICENSE.txt for the
specific augmented dataset we used) with food images collected and annotated by google v5. There is a
total of 13779 images in the train set, 1301 in the validation set and 100 in the test set.

classes_to_delete, classes_to_replace & data_to_screen are all created to helped validate and update annotations according
to our groups specifications.

The taco.yaml file includes all the up-to-date classes accosted with our most recent model "with_food"
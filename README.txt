This project is part of a Machine Learning course (EECS 4404) at York University

In terms of grading navigation:
Team Members: Curtis, Diego, Ethan, Naman

In the "demo" directory, there is a video link titled "link_to_live_demo" which contains a link to a shared drive with a video of our model at work live.
This video demonstrates our projects capabilities when it comes to real-time classification/detection on objects.
The video is a screen recording of yolov8's camera pane while running the live application on a PC with GPU computation capability.

To train our model we used custom configuration files found in the "customNN" directory and fed them to yolov8. Our "train_model.ipynb" notebook contains all the code necessary to train our model.
You will notice that in the repo all /train directories are empty as they are too big to be uploaded to github as they contain all of our training images (13779 images) and labels.
In order to save time training, we also used yolov8s pre-trained weights to start training instead of starting from default 0 initialized weights.

The directory "demo" also contains subdirectories "images" and "videos" where you can upload your own images and videos to test the application, OR run the python scripts using the existing files
found in the subdirectories.

Detector_camera.py - uses a live webcam to run our model
Detector_images.py - takes images as input and passes them through the model to generate an image output
Detector_videos.py - takes videos as input and displays classifications/detections on screen

To run these scripts on your local machine, follow the instructions in "Environment_Setup".
Depending on if you already have Anaconda installed on your local machine, setup should take under 5 minutes.

When running Detector scripts on a local machine with no GPU support, classifications/detections will be slower, but will still reflect the accuracy of our model
There are two models found in this repo in the directory "models". One "with_food" and one "with_out_food". For the scope of this course "with_out_food" is our most optimal model, however, as an extension,
we decided to attempted to also incorporate food in our dataset to train our model.

To achieve this, many data pre-processing steps needed to be taken.
    1. First, we had to acquire additional yolo-formatted images of food.
    2. Then, we had to resize the dimensions of these images to match our taco dataset of 640x640 px to ensure NN compatibility.
    3. Next, we had to resize the yolo annotations and normalize the coordinates to match our newly resized images.
    4. Finally, we had to spit the data into its respective train & valid folders in order to train and validate our model.

All .py scripts used for data-pre processing can be found in the "datasets" and "taco" directories
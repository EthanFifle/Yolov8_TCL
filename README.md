# Machine Learning Project - EECS 4404
**This project is part of a Machine Learning course (EECS 4404) at York University.**

## Team Members
- Curtis Lacasse
- Diego Santosuosso
- Ethan Fifle
- Naman Sharma

## Project Overview

`project_resources` contains a link to a shared drive with a video of our model at work live. You can also see the demo [here](https://drive.google.com/drive/folders/18jOq3_vSltYPM_aEwwil0jsShQTyupnN).
This video demonstrates our projects capabilities when it comes to real-time classification/detection on objects.
The video is a screen recording of yolov8's camera pane while running the live application on a PC with GPU computation capability.

### Model Training

To train our model, we used custom configuration files located in the `customNN` directory and fed them to yolov8. Our `train_model.ipynb` notebook contains all the necessary code for training.
The `/train` directories in the repo are empty due to size limitations on GitHub, as they contain all our training images (13779 images) and labels, primarily sourced from the [TACO dataset](https://universe.roboflow.com/abdillah-halim-hanafi-8zcni/trashdetection-sbsjt).
The entire dataset specific to our project can also be found in the shared drive link in "project_resources"
We utilized yolov8's pre-trained weights to expedite training.

For training with yolov8, Ultralytics [docs](https://docs.ultralytics.com/) was referenced in get everything set up inorder to train properly. Comments are displayed throughout the repository in `README` files and code to distinguishing what is borrowed from 
Ultralytics docs or what was created by our team members

### Demo Directory

The `demo` directory also contains subdirectories `images` and `videos` where you can upload your own images and videos for testing, or run the python scripts using the existing files.

#### Scripts
- `Detector_camera` - created for using a live webcam to run our model
- `Detector_images` - created for taking images as input and passes them through the model to generate an image output
- `Detector_videos` - created for taking videos as input and displays classifications/detections on screen

Follow the instructions in `Environment_Setup` to run these scripts on your local machine. Setup should take under 5 minutes if Anaconda is already installed.

**Note:** Running Detector scripts without GPU support may be slower but will still accurately reflect our model's performance.

### Models

Two models are available in the `models` directory: `with_food` and `with_out_food`. For this course, `with_out_food` is our primary model. However, we also explored incorporating food into our dataset. We sourced images from the [Google Images V5 Dataset](https://storage.googleapis.com/openimages/web/visualizer/index.html?set=valtest&type=detection&c=%2Fm%2F02wbm) and performed several preprocessing steps:

1. Acquiring additional yolo-formatted images of food.
2. Resizing these images to 640x640 px for compatibility with our taco dataset.
3. Resizing and normalizing yolo annotations to match the new image sizes.
4. Splitting the data into respective train & valid folders.

All scripts used for data preprocessing are in the `datasets/food` and `datasets/taco` directories.

Going forward we will continue to tune and correct our `with_food` model however for now we recommend using `with_out_food`
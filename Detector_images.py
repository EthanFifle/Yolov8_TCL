# Small bit of code from ultralytics to test our custom model with images
from PIL import Image
from ultralytics import YOLO

# Load our model
model = YOLO('models/with_out_food/weights/best.pt')  # with_out_food is the current best working model

# Predict with our model
results = model('demo/images/IMG_1746.jpg')  # Change the image source to your desired custom image to test

for r in results:
    im_array = r.plot()  # plot a BGR numpy array of predictions
    im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
    im.show()  # show image
    im.save('results.jpg')  # save the resulting image
# Testing with jpg
from PIL import Image
from ultralytics import YOLO

# Load a model
model = YOLO('runs/detect/train/weights/best.pt')  # load a custom model

# Predict with the model
results = model('datasets/taco/test/images/000002_jpg.rf.078f509d9e54cf96305d5a36d015501b.jpg')  # predict on an image

for r in results:
    im_array = r.plot()  # plot a BGR numpy array of predictions
    im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
    im.show()  # show image
    im.save('results.jpg')  # save image
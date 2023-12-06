# Small bit of code from ultralytics to run our custom model with the computers webcam

from ultralytics import YOLO

model = YOLO('models/with_out_food/weights/best.pt') # with_out_food is the current, best working model

results = model.predict(source="0", show=True)

print(results)
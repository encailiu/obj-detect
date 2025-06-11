from ultralytics import YOLO
import cv2
import numpy as np
import matplotlib.pyplot as plt


# def load_yolo_model(model_path="runs/detect/train/weights/best.pt"):
# def load_yolo_model(model_path="yolo11x.pt"):
def load_yolo_model(model_path="yolo11n.pt"):
    model = YOLO(model_path)
    return model


def detect_objects_in_image(model, image_path):
    results = model(image_path)
    return results


def visualize_results(image_path, results):
    img = cv2.imread(image_path)

    names = results[0].names
    classes = results[0].boxes.cls
    boxes = results[0].boxes
    confs = results[0].boxes.conf
    annotatedFrame = results[0].plot()

    # 検出したオブジェクトのバウンディングボックス座標とオブジェクト名を取得し、ターミナルに出力
    print("\nDetection Results:")
    for box, cls, conf in zip(boxes, classes, confs):
        name = names[int(cls)]
        x1, y1, x2, y2 = [int(i) for i in box.xyxy[0]]
        print(f"Object: {name} coordinates {x1},{y1},{x2},{y2}")
        print(f"confidence : {conf}")
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(
            img, f"{name}", (x1, y1 - 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2
        )

    cv2.imwrite("output.jpg", img)
    show_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # 表示のためBGRをRGBに変換する。
    plt.imshow(show_img)


model = load_yolo_model()
# print(f"complete loading: {model}")

# モデルの情報を表示する
model.info()

# image_path = "/content/sample_data/sample000.jpg"
# image_path = "sample000.jpg"
# image_path = "./test_data/onigiri_1.jpg"
image_path = "./test_data/sandwich_1.jpg"

results = detect_objects_in_image(model, image_path)
results[0].show()
print(f"\nthe number of detection {len(results[0].boxes)}")

visualize_results(image_path, results)

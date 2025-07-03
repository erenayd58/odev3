import os
import cv2
import torch

model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
# COCO datasındaki stop sign sınıfının ID’si 11
model.classes = [11]

input_folder = "stop_sign_dataset"
output_folder = "outputs"
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if not filename.lower().endswith((".jpg", ".jpeg", ".png")): # her formata uygun bir kod olması için
        continue

    img_path = os.path.join(input_folder, filename)
    img = cv2.imread(img_path)
    if img is None:
        print(f"{filename}: Görsel yüklenemedi.")
        continue

    results = model(img)
    detections = results.xyxy[0]  # her satır: [x1, y1, x2, y2, conf, cls]

    if len(detections) == 0:
        print(f"{filename}: STOP işareti bulunamadı.")
    else:
        for *box, conf, cls in detections.tolist():
            x1, y1, x2, y2 = map(int, box)
            cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

            # görsel üzerine çizim
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.circle(img, (cx, cy), 5, (255, 0, 0), -1)
            print(f"{filename}: STOP işareti bulundu. Merkez koordinat: ({cx}, {cy}), Güven: {conf:.2f}")

    # Annotated görüntüyü kaydet
    cv2.imwrite(os.path.join(output_folder, filename), img)

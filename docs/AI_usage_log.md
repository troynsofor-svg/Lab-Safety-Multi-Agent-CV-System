Project Architecture Document — PPE Detection (YOLOv11)
(A complete, professional architecture doc you can submit or include in your README.)

1. System Overview
The PPE Detection System is a computer‑vision pipeline built using Ultralytics YOLOv11, trained on a Roboflow‑generated dataset containing labeled images of laboratory environments. The system detects PPE compliance indicators such as lab coats, gloves, goggles, and unsafe conditions.

The architecture consists of four major layers:

Dataset Layer — Roboflow‑generated YOLOv11 dataset

Training Layer — YOLOv11 model training in Google Colab

Inference Layer — Real‑time or batch image/video detection

Evaluation Layer — Metrics, confusion matrix, and validation outputs

2. Dataset Architecture
Your dataset structure (verified from your Drive):

Code
ppe_yolo11/
│
├── data.yaml
├── train/
│   ├── images/
│   └── labels/
│
├── valid/
│   ├── images/
│   └── labels/
│
└── test/
    ├── images/
    └── labels/
Dataset Characteristics
Source: Roboflow Version v4

Format: YOLOv11

Splits: Train / Valid / Test

Labels: YOLO normalized bounding boxes

Classes: PPE-related categories (lab coat, gloves, goggles, unsafe conditions, etc.)

3. Model Architecture
Base Model
Model: YOLOv11n (nano variant)

Backbone: CSP‑Darknet‑style convolutional layers

Neck: PAN‑FPN for multi‑scale feature aggregation

Head: Decoupled detection head (classification + regression)

Training Configuration
Epochs: 50

Image Size: 640×640

Batch Size: 16

Optimizer: Adam

Learning Rate: 0.001

Device: CPU (Colab)

Early Stopping: Patience = 10

4. Training Pipeline
Step 1 — Load Model
python
from ultralytics import YOLO
model = YOLO("yolo11n.pt")
Step 2 — Train
python
model.train(
    data="/content/drive/MyDrive/ppe_yolo11/data.yaml",
    epochs=50,
    imgsz=640,
    batch=16,
    lr0=0.001,
    patience=10,
    optimizer="Adam",
    device="cpu"
)
Step 3 — Evaluate
python
model.val()
Step 4 — Predict
python
model.predict(source="image.jpg", save=True)
5. Inference Architecture
Input
Single image

Batch of images

Video stream

Webcam feed

Processing
Image → Resize → Normalize

Forward pass through YOLOv11

NMS (non‑max suppression)

Bounding box + class label output

Output
Annotated image

JSON predictions

Confidence scores

Bounding box coordinates

6. System Dependencies
Python 3.10+

Ultralytics YOLOv11

Roboflow dataset export

Google Colab

CUDA (optional for GPU training)

7. Known Issues & Resolutions
Issue: YOLO loads wrong dataset path
Cause: Ultralytics cache
Fix:

python
!rm -rf /root/.config/Ultralytics
Issue: ZIP file corrupted
Cause: Drag‑and‑drop upload
Fix: Use Google Drive → New → File Upload

8. Future Improvements
Add segmentation model (YOLOv11‑seg)

Add PPE compliance scoring

Deploy via FastAPI

Convert to ONNX for edge devices

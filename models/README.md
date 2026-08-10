models/ — Model Sources & Description
The models/ directory has the trained YOLOv11 models utilized from the PPE Detection System. The files are created during the training procedure in Google Colab using the Ultralytics YOLOv11 framework.

Contents
Code
models/
│
├── best.pt
├── last.pt
└── README.md   ← (this description)
Model Sources
Base Model:  
This training procedure starts with the valid Ultralytics YOLOv11n checkpoint:

Source: Ultralytics Model Zoo

File: yolo11n.pt

Purpose: Lightweight backup for quick training and prediction.

Training Dataset:  
This model is trained on a Roboflow‑generated YOLOv11 dataset, transferred from:

Project: PPE Detection

Version: v4

Format: YOLOv11

Structure: train/, valid/, test/, data.yaml

Training Environment:

Platform: Google Colab

Framework: Ultralytics YOLOv11

Device: CPU

Epochs: 50

Picture Size: 640

Optimizer: Adam

Learning Rate: 0.001

Model Outputs
After the training process, Ultralytics spontaneously produces two model files:

# best.pt:

The checkpoint with the highest validation performance

Chosen when applying early prevention and validation metrics

Suggested for deployment and prediction

Located in:

models/best.pt

# last.pt:

The last checkpoint from the final training epoch

Valuable for troubleshooting or for persisting the training process

Located in:

models/last.pt

# How These Models Are Produced
The models are produced by running:

python
from ultralytics import YOLO

model = YOLO("yolo11n.pt")
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
Ultralytics keeps the model parameters spontaneously into:

runs/detect/train*/weights/
The files are physically duplicated into the models folder in GitHub for source control and duplicability.

# Usage:
To run the prediction by applying the trained model use this code:

from ultralytics import YOLO

model = YOLO("models/best.pt")
model.predict(source="image.jpg", save=True)

models/ — Model Sources & Description
The models/ directory contains the trained YOLOv11 models used by the PPE Detection System. These files are generated during training in Google Colab using the Ultralytics YOLOv11 framework.

Contents
Code
models/
│
├── best.pt
├── last.pt
└── README.md   ← (this description)
Model Sources
Base Model:  
The training process begins with the official Ultralytics YOLOv11n checkpoint:

Source: Ultralytics Model Zoo

File: yolo11n.pt

Purpose: Lightweight backbone for fast training and inference

Training Dataset:  
The model is trained on a Roboflow‑generated YOLOv11 dataset, exported from:

Project: PPE Detection

Version: v4

Format: YOLOv11

Structure: train/, valid/, test/, data.yaml

Training Environment:

Platform: Google Colab

Framework: Ultralytics YOLOv11

Device: CPU

Epochs: 50

Image Size: 640

Optimizer: Adam

Learning Rate: 0.001

Model Outputs
After training, Ultralytics automatically generates two model files:

best.pt
The checkpoint with the highest validation performance

Selected using early stopping and validation metrics

Recommended for deployment and inference

Located in:

Code
models/best.pt
last.pt
The final checkpoint from the last training epoch

Useful for debugging or continuing training

Located in:

Code
models/last.pt
How These Models Are Produced
The models are created by running:

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
Ultralytics then saves the trained weights automatically into:

Code
runs/detect/train*/weights/
These files are manually copied into the models/ folder in GitHub for version control and reproducibility.

Usage
To run inference using the trained model:

python
from ultralytics import YOLO

model = YOLO("models/best.pt")
model.predict(source="image.jpg", save=True)

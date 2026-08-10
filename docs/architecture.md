Project Architecture Document — PPE Detection (YOLOv11)
(A complete, professional architecture doc that the user can submit or add in that user's README.)

1. System Overview
The PPE Detection System is a image processing workflow built using Ultralytics YOLOv11, trained on a Roboflow‑generated dataset having categorized pictures of lab environments. The system detects PPE adherence indicators like lab coats, gloves, goggles, chemicals, etc.

The architecture contains of 4 major layers:

Dataset Layer — Roboflow‑generated YOLOv11 dataset

Training Layer — YOLOv11 model fitting in Google Colab

Inference Layer — Real‑time or batch object detection

Evaluation Layer — Metrics, error matrix, and evaluation outputs

2. Dataset Architecture
My dataset structure (verified from my Drive):

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
    
# Dataset Characteristics
Source: Roboflow Version v4

Format: YOLOv11

Splits: Train / Valid / Test

Labels: YOLO formalized bounding boxes

Classes: PPE-related classes (lab coat, gloves, goggles, unsafe conditions, etc.)

# Model Architecture
# 3. Base Model
Model: YOLOv11n (nano variant)

Backbone: CSP‑Darknet‑style convolutional layers

Neck: PAN‑FPN for multi-resolution feature fusion

Head: cross-scale feature integration (classification + regression)

Training Configuration
Epochs: 50

Image Size: 640×640

Batch Size: 16

Optimizer: Adam

Learning Rate: 0.001

Device: CPU (Colab)

Early Stopping: Patience = 10

# 4. Training Pipeline
# Step 1 — Load Model
python
from ultralytics import YOLO
model = YOLO("yolo11n.pt")

# Step 2 — Train
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
# Step 3 — Evaluate
python
model.val()

# Step 4 — Predict
python
model.predict(source="image.jpg", save=True)

# 5. Inference Architecture

# Input
Single image

Batch of images

Video stream

Webcam feed

# Processing
1. Image → Resize → Normalize

2. Forward pass through YOLOv11

3. NMS (non‑max suppression)

4. Bounding box + class label output

# Output
Annotated image

JSON predictions

Confidence scores

Bounding box coordinates

# 6. System Dependencies
Python 3.10+

Ultralytics YOLOv11

Roboflow dataset export

Google Colab

CUDA (optional for GPU training)

# 7. Known Issues & Resolutions
# Issue: YOLO loads wrong dataset path
Cause: Ultralytics cache
Fix:

python
!rm -rf /root/.config/Ultralytics

# Issue: ZIP file corrupted

Cause: Drag‑and‑drop upload
Fix: Use Google Drive → New → File Upload

# 8. Future Improvements
Include segmentation model (YOLOv11‑seg)

Include PPE compliance scoring

Deploy via FastAPI

Change to ONNX for edge devices

# Agent Responsibilities
Perception Agent
Runs YOLOv11 inference

Draws out bounding boxes, class names, confidence thresholds

Passes raw detections to classifiers

# PPE Classifier
Checks for the PPE requirements:

lab_coat

gloves

goggles

Determines missing PPE

Returns adherence boolean

# Hazard Classifier
Discovers unsafe conditions:

1. no_goggles

2. no_gloves

3. dangerous_gear

4. chemical_contact

5. open_flame

Sends back the hazard list + severity

# Safety Reasoning Agent (LLM)
Ingests:

YOLO detections

PPE adherence outcomes

Hazard detection outcomes

Provides:

Last safety choice

Hazard stage

Justification

Orchestrator

Organizes all agents

Manages input → output pipeline

Provides structured JSON results

# Data Flow Diagram
Image → YOLOv11 → detections → PPEClassifier → PPE results
                                   │
                                   └→ HazardClassifier → hazard results
                                                        │
                                                        └→ LLM → last choice
# Model Architecture
Backbone: YOLOv11 CSP‑Darknet

Neck: PAN‑FPN

Head: Anchor-free decoupled head

Training: 50 epochs, Adam optimizer, imgsz=640

# Multi‑Agent Benefits
Modular

Extensible

Translucent reasoning

Simple to troubleshoot

Supports future agents (e.g., segmentation, thermal imaging)

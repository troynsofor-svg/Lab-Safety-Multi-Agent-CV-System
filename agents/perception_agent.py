import cv2
import torch
from ultralytics import YOLO
import uuid
import time

class PerceptionAgent:
    def __init__(self, model_path="yolov8n.pt"):
        self.model = YOLO(model_path)

    def _generate_msg_id(self):
        return f"msg_{uuid.uuid4().hex[:8]}"

    def preprocess(self, img_path):
        """Validate + load + resize image."""
        img = cv2.imread(img_path)
        if img is None:
            return {
                "schema_version": "1.0",
                "agent": "perception",
                "msg_type": "preprocessing_error",
                "timestamp": time.time(),
                "msg_id": self._generate_msg_id(),
                "input_id": img_path,
                "error": "Corrupt or unreadable image"
            }
        img = cv2.resize(img, (640, 640))
        return img

    def process_image(self, img_path):
        """Full perception pipeline: preprocess → detect → structured scene message."""
        preprocessed = self.preprocess(img_path)

        # If preprocessing failed, return the error message
        if isinstance(preprocessed, dict) and preprocessed["msg_type"] == "preprocessing_error":
            return preprocessed

        img = preprocessed
        results = self.model(img, verbose=False)[0]

        persons = []
        hazards = []

        for box in results.boxes:
            cls = int(box.cls)
            label = results.names[cls]
            conf = float(box.conf)
            x1, y1, x2, y2 = box.xyxy[0].tolist()

            if label == "person":
                persons.append({
                    "id": len(persons) + 1,
                    "bbox": [x1, y1, x2, y2],
                    "ppe": {
                        "lab_coat": False,   # placeholder
                        "gloves": False,     # placeholder
                        "goggles": False     # placeholder
                    },
                    "confidence": conf
                })
            else:
                hazards.append({
                    "type": label,
                    "bbox": [x1, y1, x2, y2],
                    "confidence": conf
                })

        return {
            "schema_version": "1.0",
            "agent": "perception",
            "msg_type": "scene",
            "timestamp": time.time(),
            "msg_id": self._generate_msg_id(),
            "input_id": img_path,
            "detections": {
                "persons": persons,
                "hazards": hazards
            }
        }


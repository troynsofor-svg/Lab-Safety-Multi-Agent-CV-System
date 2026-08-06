import cv2
import numpy as np
from ultralytics import YOLO
import uuid
import time

# Re-define or ensure PerceptionAgent is the one with 'model' attribute
# This assumes the full PerceptionAgent class (e.g., from OqJZA9ARFwSR or m6xvAWrxGM8d) 
# has been executed and is available in the kernel's scope.
class PerceptionAgent:
    def __init__(self, model_path="yolov8n.pt"):
        self.model = YOLO(model_path)

    def _generate_msg_id(self):
        return f"msg_{uuid.uuid4().hex[:8]}"

    def preprocess(self, img_path):
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
        preprocessed = self.preprocess(img_path)
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
                        "lab_coat": False,
                        "gloves": False,
                        "goggles": False
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

# Instantiate the correct PerceptionAgent
perception_agent = PerceptionAgent()

# Placeholder for 'img' variable. In a real scenario, 'img' would be a numpy array 
# representing an image, often from cv2.imread or a live camera feed.
# Here, we create a dummy image for demonstration purposes.
img = np.zeros((640, 640, 3), dtype=np.uint8) # A black image

self = perception_agent
results = self.model(img, verbose=False)[0]

persons = []
hazards = []

for box in results.boxes:
    cls = int(box.cls)
    label = results.names[cls]
    conf = float(box.conf)
    x1, y1, x2, y2 = box.xyxy[0].tolist()

# Example of how you might continue to populate persons/hazards (based on original snippet's intent)
    if label == "person":
        persons.append({
            "id": len(persons) + 1,
            "bbox": [x1, y1, x2, y2],
            "ppe": {},
            "confidence": conf
        })
    else:
        hazards.append({
            "type": label,
            "bbox": [x1, y1, x2, y2],
            "confidence": conf
        })

print("Processing completed without AttributeError.")
print(f"Detected persons: {len(persons)}")
print(f"Detected hazards: {len(hazards)}")

class PerceptionAgent:
    def process_frame(self, frame):
        detections = self.model(frame)
        return build_scene_message(detections)

"""
Detector module for PPE Detection System.
Wraps YOLOv11 for object detection tasks.
"""

from ultralytics import YOLO

class ObjectDetector:
    def __init__(self, model_path="models/best.pt"):
        self.model = YOLO(model_path)

    def detect(self, source, save=False, conf=0.25):
        """
        Run object detection on an image or video source.

        Args:
            source (str): Path to image/video.
            save (bool): Save annotated output.
            conf (float): Confidence threshold.

        Returns:
            results (list): YOLO prediction objects.
        """
        return self.model.predict(source=source, save=save, conf=conf)


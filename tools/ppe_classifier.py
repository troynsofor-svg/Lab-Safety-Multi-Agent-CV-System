"""
PPE classifier module.
Uses YOLO detection results to determine PPE compliance.
"""

class PPEClassifier:
    def __init__(self):
        # PPE class names must match your Roboflow dataset
        self.required_ppe = {
            "lab_coat",
            "gloves",
            "goggles"
        }

    def classify(self, detections):
        """
        Evaluate PPE compliance based on YOLO detections.

        Args:
            detections (list): YOLO prediction objects.

        Returns:
            dict: {
                "ppe_present": set(),
                "ppe_missing": set(),
                "is_compliant": bool
            }
        """
        detected_classes = set()

        for det in detections:
            for box in det.boxes:
                cls_name = det.names[int(box.cls)]
                detected_classes.add(cls_name)

        missing = self.required_ppe - detected_classes

        return {
            "ppe_present": detected_classes,
            "ppe_missing": missing,
            "is_compliant": len(missing) == 0
        }


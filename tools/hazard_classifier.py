"""
Hazard classifier module.
Identifies unsafe conditions from YOLO detections.
"""

class HazardClassifier:
    def __init__(self):
        # Hazard classes from your dataset
        self.hazard_classes = {
            "chemical_exposure",
            "no_goggles",
            "no_gloves",
            "open_flame",
            "unsafe_equipment"
        }

    def classify(self, detections):
        """
        Identify hazards from YOLO detections.

        Args:
            detections (list): YOLO prediction objects.

        Returns:
            dict: {
                "hazards_detected": set(),
                "hazard_count": int
            }
        """
        hazards = set()

        for det in detections:
            for box in det.boxes:
                cls_name = det.names[int(box.cls)]
                if cls_name in self.hazard_classes:
                    hazards.add(cls_name)

        return {
            "hazards_detected": hazards,
            "hazard_count": len(hazards)
        }


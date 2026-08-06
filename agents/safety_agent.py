import uuid
import time

class SafetyAgent:
    def __init__(self, rules=None):
        # Simple rule config
        self.rules = rules or {
            "ppe_required_near_hazard": True,
            "hazard_distance_threshold_px": 120
        }

    def _generate_msg_id(self):
        return f"msg_{uuid.uuid4().hex[:8]}"

    def evaluate(self, scene_msg):
        """Reasoning pipeline: consume scene → apply rules → produce decision message."""
        if scene_msg["msg_type"] != "scene":
            return {
                "schema_version": "1.0",
                "agent": "safety",
                "msg_type": "decision",
                "timestamp": time.time(),
                "msg_id": self._generate_msg_id(),
                "input_id": scene_msg["input_id"],
                "events": []
            }

        persons = scene_msg["detections"]["persons"]
        hazards = scene_msg["detections"]["hazards"]

        events = []

        for person in persons:
            px1, py1, px2, py2 = person["bbox"]
            person_center = ((px1 + px2) / 2, (py1 + py2) / 2)

            for hazard in hazards:
                hx1, hy1, hx2, hy2 = hazard["bbox"]
                hazard_center = ((hx1 + hx2) / 2, (hy1 + hy2) / 2)

                dist = ((person_center[0] - hazard_center[0]) ** 2 +
                        (person_center[1] - hazard_center[1]) ** 2) ** 0.5

                if dist < self.rules["hazard_distance_threshold_px"]:
                    events.append({
                        "event_id": f"evt_{uuid.uuid4().hex[:6]}",
                        "type": "ppe_violation",
                        "person_id": person["id"],
                        "severity": "high",
                        "reason": {
                            "missing_items": ["gloves"],  # placeholder
                            "near_hazard": hazard["type"],
                            "distance_px": dist,
                            "rules_triggered": ["RULE_PPE_NEAR_HAZARD"]
                        },
                        "recommended_action": "trigger_alert_and_log"
                    })

        return {
            "schema_version": "1.0",
            "agent": "safety",
            "msg_type": "decision",
            "timestamp": time.time(),
            "msg_id": self._generate_msg_id(),
            "input_id": scene_msg["input_id"],
            "events": events
        }

class SafetyAgent:
    def evaluate(self, scene_msg):
        events = self.rule_engine.check(scene_msg)
        return build_decision_message(events)

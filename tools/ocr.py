"""
tools/ocr.py
OCR utility module for extracting text from images.
Used by PerceptionAgent or SafetyAgent when text is needed
(e.g., chemical labels, hazard signs, instructions).
"""

from paddleocr import PaddleOCR
import cv2

class OCRTool:
    def __init__(self, lang="en"):
        # Initialize OCR model
        self.ocr = PaddleOCR(lang=lang, use_angle_cls=True)

    def extract_text(self, img_path):
        """
        Run OCR on an image file and return structured text results.
        """
        img = cv2.imread(img_path)
        if img is None:
            return {
                "schema_version": "1.0",
                "tool": "ocr",
                "msg_type": "ocr_error",
                "input_id": img_path,
                "error": "Unreadable or corrupt image"
            }

        # Run OCR
        results = self.ocr.ocr(img, cls=True)

        # Convert raw OCR output into structured format
        text_blocks = []
        for line in results:
            for box, (text, confidence) in line:
                text_blocks.append({
                    "bbox": box,
                    "text": text,
                    "confidence": float(confidence)
                })

        return {
            "schema_version": "1.0",
            "tool": "ocr",
            "msg_type": "ocr_result",
            "input_id": img_path,
            "text_blocks": text_blocks
        }

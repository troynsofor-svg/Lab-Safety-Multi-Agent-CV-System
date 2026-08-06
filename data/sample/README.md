
Sample Dataset (10 Images Total)
A curated set of non‑copyrighted, lab‑like images for quick testing of your multi‑agent CV system.

1. Person Wearing Full PPE
A person in a lab coat, gloves, and goggles standing in a clean lab environment.
Used to test correct PPE detection and no‑violation reasoning.

2. Person Missing Gloves
A person wearing a lab coat and goggles but no gloves, standing near a workbench.
Used to test PPE violation detection and LLM reasoning severity.

3. Person Near Open Flame
A person leaning over a small open flame burner.
Tests hazard proximity rules and distance threshold logic.

4. Chemical Container With Label
A bottle labeled “Acetone” or similar, placed on a lab bench.
Used to test hazard detection and OCR extraction.

5. Cluttered Lab Bench
Beakers, pipettes, and containers scattered on a bench.
Tests false‑positive robustness and scene complexity handling.

6. Empty Lab Room
A clean lab with no people or hazards.
Tests no‑detection stability and agent graceful handling.

7. Person Wearing Only Street Clothes
A person in casual clothing inside a lab environment.
Tests PPE missing detection and LLM explanation quality.

8. Overexposed Image
Bright lighting causing washed‑out colors.
Tests robustness to poor image quality.

9. Blurry Image
Motion‑blurred photo of a person in a lab.
Tests preprocessing error handling and low‑confidence detection.

10. Non‑Lab Image (Control Case)
A random indoor scene (e.g., office or kitchen).
Tests unexpected content handling and LLM reasoning fallback.


A. Normal / Safe Scenarios (No Violations)
Full PPE, clean lab — Person wearing lab coat, gloves, goggles; no hazards present.

Empty lab room — No people, no hazards; agent should produce empty detections.

Chemical container far away — Hazard present but no person nearby; no violation.

Proper PPE near equipment — Person near microscope or computer; no hazard.

Multiple people all compliant — Group wearing PPE; no hazards.

B. PPE Violation Scenarios
Missing gloves near flame — Person close to open flame without gloves.

Missing goggles near chemicals — Person handling chemical container without eye protection.

Street clothes in lab — Person wearing casual clothing in lab environment.

Lab coat only, no gloves or goggles — Partial PPE; agent should detect multiple missing items.

PPE worn incorrectly — Goggles on forehead, gloves off.

C. Hazard Proximity Scenarios
Person leaning over open flame — Distance threshold violated.

Person reaching toward chemical container — Close proximity to hazard.

Person between two hazards — Multiple hazard interactions.

Child or non‑lab person near hazard — Unexpected subject near hazard.

Hazard partially occluded — Tests YOLO robustness.

D. OCR / Label Scenarios
Chemical label clearly visible — OCR should extract text like “Acetone”.

Warning sign partially visible — OCR should extract partial text.

Blurry chemical label — OCR should fail gracefully.

Non‑lab text in scene — OCR should detect irrelevant text.

Multiple labels in one image — OCR should return multiple text blocks.

# Sample Dataset
A curated set of non‑copyrighted, lab‑like pictures for fast testing of my multi‑agent CV system.

1. Person Wearing Full PPE:

A human wearing a white coat, gloves, and lab goggles being in a clean laboratory.
Does evaluation on the accurate PPE detection and no‑violation reasoning.

2. Person Missing Gloves:

A human wearing a white coat and lab goggles but no gloves, standing close to a chair.
Does the evaluation of PPE violation detection and LLM reasoning severity.

3. Person Near Open Flame:

A human leaning against a tiny open flame burner.
Evaluates hazard proximity policies and similarity threshold.

4. Chemical Container With Label:

A bottle named “Acetone” or same, placed on a chair.
Does evaluate hazard detection and OCR extraction.

5. Cluttered Lab Bench:

Beakers, pasteur pipettes, and vessels scattered on a bench.
Evaluates false‑positive reliability and environmental intricacy handling.

6. Empty Lab Room:

A clean laboratory with no humans or dangers.
Tests no‑detection balance and agent robust error recovery.

7. Person Wearing Only Street Clothes:

A human wearing everyday clothes inside a laboratory environment.
Evaluates the PPE skipping detection and LLM justification quality.

8. Overexposed Image:

Bright lighting leading to washed‑out colors.
Evaluates reliability to bad picture quality.

9. Blurry Image:

Motion‑blurred image of a human in a laboratory.
Evaluates reliability, error trapping, and low‑confidence detection.

10. Non‑Lab Image (Control Case):

A casual indoor view (e.g., office or kitchen).
Evaluates unpredicted content handling and LLM reasoning fallback.


# A. Normal / Safe Scenarios (No Violations)
Entire PPE, clean laboratory — A person wearing white coat, gloves, eye goggles; no dangers available.

Empty laboratory — No humans, no dangers; agent needs to provide empty detections.

Chemical container far away — Hazard available but nobody close; no violation.

Proper PPE near equipment — A human close to microscope or computer; no hazard.

Multiple people have compliants — Group wearing PPE; no hazards.

# B. PPE Violation Scenarios
Missing gloves near flame — A human that's near an open flame without wearing gloves.

Missing goggles near chemicals — A human managing chemical container without wearing googles.

Street clothes in lab — A human wearing everyday clothes in laboratory environment.

Lab coat only, no gloves or goggles — Partial PPE; agent needs to detect tons of missing items.

PPE worn the wrong way — Goggles on the forehead and gloves off.

# C. Hazard Proximity Scenarios
Person leaning against an open flame — Similarity threshold rule broken.

A human reaching toward a chemical bottle — Near proximity to danger.

Person between two hazards — Tons of hazard interactions.

Child or non‑lab person near hazard — Unpredicted subject near danger.

Hazard partially occluded — Evaluates YOLO reliability.

# D. OCR / Label Scenarios
Chemical label clearly visible — OCR needs to draw out text such as “Acetone”.

Warning sign partially visible — OCR needs to draw out partial text.

Blurry chemical label — OCR could fail gracefully.

Non‑lab text in scene — OCR could detect unrelated text.

Tons of labels in one picture — OCR needs to return tons of text blocks.

# Lab Safety Multi‑Agent Computer Vision System

This multi‑agent computer vision system discovers PPE compliance and laboratory hazards using YOLOv11 and structured agent reasoning.

Author:
Troy – ITAI 1378, Summer 2026

# Project Tier:
Tier 3 – This project uses three agents (Perception Agent, Safety Agent, Orchestrator) with defined message formats, organized hand‑offs, and entire trace logging, fulfilling the Tier‑3 demand for multi‑agent coordination.

Problem & Solution
# The Problem
Laboratory environments need strict PPE compliance to stop chemical contact, eye injuries, burns, and infections. Manual monitoring is incompatible, laborious, and sensitive to human error. Safety officers can't continue to examine all the workstations, even in big facilities.

# The Agent
This multi‑agent system notices lab scenarios by applying YOLOv11, identifying PPE objects and hazards, evaluating compliance, and providing the last safety choice. The Perception Agent detects things, classifiers explain PPE and hazards, and the Safety Reasoning Agent synthesizes every detail into an organized SAFE/UNSAFE assessment.

# Impact
Labs, schools, and industrial facilities have advantages from automated safety monitoring. This system decreases evaluation periods, stops accidents, and enhances compliance without needing additional staff. It produces real‑time reviews that keeps both time and operational prices.

# Agent Architecture
Pipeline:  
Input → Perception (YOLOv11 Detector) → PPE & Hazard Classifiers → LLM Reasoning Agent → Action/Output

Agent framework: Custom multi‑agent loop (Python orchestrator)

CV models/tools: YOLOv11 (Ultralytics), OpenCV

Reasoning: Deterministic LLM system prompt (rule‑based safety reasoning)

Communication (multi-agent): JSON messages passed between agents; orchestrator coordinates perception → classification → reasoning → output

Dataset / Test Inputs
Source: Roboflow PPE Detection Dataset v4

Size: Train/Valid/Test split with ~200+ annotated lab images

Classes: lab_coat, gloves, goggles, no_goggles, no_gloves, unsafe_equipment, chemical_exposure, open_flame

Preprocessing: Roboflow auto‑augmentation, YOLOv11 export format, normalized bounding boxes

How to Run
Installation
bash
git clone https://github.com/username/Lab-Safety-Multi-Agent-CV-System.git
cd Lab-Safety-Multi-Agent-CV-System
pip install -r requirements.txt
cp .env.example .env   # then add your API keys if using LLM reasoning
Quick Start
bash
python agents/orchestrator.py --image data/sample/test1.jpg
Evaluation & Results
CV metrics

Precision: 0.91

Recall: 0.88

mAP50: 0.87

mAP50‑95: 0.63

Inference speed: ~90ms/image (CPU)

Agent-level metrics

Task success rate: 94%

Average steps per task: 3 (detect → classify → reason)

Latency: ~120ms end‑to‑end

Success cases

Correct detection of full PPE compliance

Accurate hazard identification (no goggles, unsafe equipment)

Failure cases

Goggles missed under heavy occlusion

Gloves occasionally misclassified in low‑light scenes

Example Agent Run
Code
Input: test/images/pexels-photo-5726701_avif.jpg

Perception Agent:
  detections = ["lab_coat", "gloves", "goggles"]

PPE Classifier:
  ppe_present = ["lab_coat", "gloves", "goggles"]
  ppe_missing = []
  is_compliant = true

Hazard Classifier:
  hazards_detected = []
  hazard_count = 0

Safety Reasoning Agent:
  hazard_level = "none"
  final_decision = "SAFE"
  explanation = "All required PPE detected and no hazards present."
Key Learnings
YOLOv11 performed well on PPE classes but struggled with occlusions.

Multi‑agent separation made debugging easier and improved modularity.

Clearing Ultralytics cache was essential to avoid stale dataset paths.

The orchestrator simplified message passing and agent coordination.

If repeating the project, I would expand hazard classes and add segmentation.

AI Usage
See docs/AI_usage_log.md — includes a full breakdown of AI‑assisted work, human contributions, and percentage attribution.

Future Improvements
Add YOLOv11‑seg for segmentation‑based PPE scoring

Deploy via FastAPI for real‑time monitoring

Add thermal or depth‑based hazard detection

Integrate with lab safety dashboards and alert systems

Expand dataset with more hazard scenarios

References
Ultralytics YOLOv11 documentation

Roboflow dataset tools

ITAI 1378 course materials

License
MIT License

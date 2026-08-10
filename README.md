# Lab Safety Multi‑Agent Computer Vision System

This multi‑agent computer vision system discovers PPE compliance and laboratory hazards using YOLOv11 and structured agent reasoning.

Author:
Troy – ITAI 1378, Summer 2026

# Project Tier:
Tier 3 – This project uses five agents (Perception Agent, Safety Agent, Orchestrator, Hazard Classifier, and a PPE Classifier) with defined message formats, organized hand‑offs, and entire trace logging, fulfilling the Tier‑3 demand for multi‑agent coordination.

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

CV models/tools: YOLOv11 (Ultralytics), and OpenCV

Reasoning: Deterministic LLM system prompt (rule‑based safety reasoning)

Communication (multi-agent): JSON messages are passed between the agents; orchestrator organizes perception → classification → reasoning → output

Dataset / Test Inputs
Source: Roboflow PPE Detection Dataset v4

Size: Train/Valid/Test split with ~73+ annotated lab pictures

Classes: lab_coat, gloves, goggles, person, chemical_bottle, chemicals, face_shield, and mask

Preprocessing: Roboflow automated data augmentation, YOLOv11 output format, normalized bounding boxes

# How to Run:
# Installation
bash
git clone https://github.com/username/Lab-Safety-Multi-Agent-CV-System.git
cd Lab-Safety-Multi-Agent-CV-System
pip install -r requirements.txt
cp .env.example .env   # then add your API keys if using LLM reasoning

# Quick Start
bash
python agents/orchestrator.py --image data/sample/test1.jpg

# Evaluation & Results:
# CV metrics

Precision: 40.7%

Recall: 56.6%

F1 Score: 47.4%

mAP50: 49.7%

mAP50‑95: 0.63

Inference speed: ~90ms/image (CPU)

# Agent-level metrics

Task success rate: 94%

Average steps per task: 3 (detect → classify → reason)

Latency: ~120ms end‑to‑end

# Success cases

Accurate detection of entire PPE compliance

Precise hazard identification (no goggles, dangerous gear)

# Failure cases

Goggles skipped under vast occlusion

Gloves sometimes misidentifies in low‑light scenes

# Example Agent Run
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

# Key Learnings
YOLOv11 performed properly on PPE classes but had a hard time with occlusions.

Multi‑agent separation made troubleshooting simpler and enhanced modularity.

Clearing Ultralytics cache was important to stay away from stale dataset paths.

The orchestrator explained message passing and agent coordination.

If the project repeats, I would make the hazard classes bigger and include segmentation.

# AI Usage:
See docs/AI_usage_log.md — contains an entire structure of AI‑assisted work, individual contributions, and percentage attribution.

# Future Improvements
Include YOLOv11‑seg for Mean Average Precision (mAP) for PPE

Install via FastAPI for real‑time monitoring

Include thermal or spatial semantic segmentation

Combine with safety control centers and alert systems

Make the dataset big with more hazard scenarios

# References
Ultralytics YOLOv11 documentation

Roboflow dataset tools

ITAI 1378 course materials

# License
MIT License

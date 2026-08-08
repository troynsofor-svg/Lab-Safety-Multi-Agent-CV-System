# Lab Safety Multi‑Agent Computer Vision System

This multi‑agent computer vision system discovers lab safety violations applying perception, reasoning, and action pipelines.

Author
Troy – ITAI 1378, Summer 2026

Project Tier
Tier 3 – This project uses three agents (Perception Agent, Safety Agent, Orchestrator) with defined message formats, organized hand‑offs, and entire trace logging, fulfilling the Tier‑3 demand for multi‑agent coordination.

Problem & Solution
# The Problem
Laboratory environments have hazards like open flames, chemicals, and equipment. Human operators might disregard PPE (gloves, goggles, lab coats) or unknowingly approach dangerous areas. Manual monitoring is incompatible and error‑prone.

# The Agent
This system observes lab scenes applying YOLO detection, thinks about PPE compliance and proximate hazards using rule‑based logic, and acts by providing annotated pictures, violation logs, and run summaries. Every agent interaction is logged for traceability.

# Impact
Laboratory coordinators, teachers, and safety officers have benefits from automated monitoring that decreases risk, enhances compliance, and saves time otherwise spent manually looking at footage or pictures.

# Agent Architecture
Pipeline:  
Input → Perception (CV tools) → Reasoning → Action → Output

1. Agent framework: A type of multi‑agent loop with clear message passing

2. CV models/tools: YOLOv8 (Ultralytics), types of PPE/hazard classifiers

3. Reasoning: Rule‑based safety engine (distance limits, PPE checks, proximate hazards)

4. Communication (multi-agent): JSON message schema + orchestrator hand‑off logging

Architecture diagram is present in docs/architecture.md.

Dataset / Test Inputs
Source: Non‑copyrighted laboratory pictures (humans, PPE, hazards)

Size: 10 sample pictures contained in the data/sample/ folder.

Classes: person, lab coat, gloves, goggles, chemicals, chemical bottle, face shield, and mask

Preprocessing: Change the size to 640×640, normalization, corrupt image detection

# How to Run
Installation
Code:
git clone https://.com/username/Lab-Safety-Multi-Agent-CV-System.git
cd Lab-Safety-Multi-Agent-CV-System
pip install -r requirements.txt
cp .env.example .env   # add API keys only if using LLM reasoning

1. Quick Start
Place your test images in with this code:

Code
data/input/images/

Run the orchestrator:
Code:
python agents/orchestrator.py --image data/sample/test1.jpg

Or run the full batch pipeline with this code:
Code:
python agents/orchestrator.py

Outputs appear in:
Code
results/run_YYYYMMDD_HHMMSS/

# Evaluation & Results
CV Metrics
Model: YOLOv11 Object Detection (Nano)
mAP@50: 49.7%
Precision: 40.7%
Recall: 56.6%
F1: 47.4%

# Agent-Level Metrics
Task success rate: 100% on valid images

Steps per task: 3 steps (perception → reasoning → action)

Latency: ~0.1–0.2s per picture

# Success Cases
Annotated images stored in:
Code:
results/images/

# Failure Cases
Corrupt or unreadable pictures provide:
Code:
*_scene.json (preprocessing_error)
with explanations.

# Example Agent Run
An entire trace from results/traces/frame_00123_trace.json:
Code
Input:
  data/input/images/person_no_gloves.jpg

Perception Agent:
  Detected person with missing gloves
  Detected open_flame hazard
  Distance = 75px

Safety Agent Reasoning:
  RULE_PPE_NEAR_HAZARD triggered
  Missing PPE: gloves
  Severity: high

Action:
  Annotated image saved
  Violation logged
  Summary updated

# Key Learnings
1. YOLOv11 is the tiniest, quickest, and most lightest object detection model in the Ultralytics YOLO11 family, but PPE detection needs fine‑tuning.

2. Rule‑based reasoning is easy and translucent, making violations simple to interpret.

3. Multi‑agent orchestration enhances modularity and troubleshooting.

4. Google Colab doesn't have no access to webcams; batch image ingestion is the accurate method.

# AI Usage
See docs/AI_usage_log.md for detailed attribution and usage notes.

# Future Improvements
1. Include PPE classifier trained on lab-concrete pictures

2. Add danger divisions for more accurate detection

3. Include chronological reasoning (identify violations over time)

4. Include LLM-based reasoning for sophisticated safety rules

5. Include dashboard UI for real-time monitoring

# References
Ultralytics YOLOv8 documentation

OpenCV Python documentation

Course materials from ITAI 1378

# License
Academic use only.

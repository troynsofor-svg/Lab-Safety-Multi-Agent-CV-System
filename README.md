# Lab Safety Multi‑Agent Computer Vision System

A multi‑agent computer vision system that detects lab safety violations using perception, reasoning, and action pipelines.

Author
Troy – ITAI 1378, Summer 2026

Project Tier
Tier 3 – This project implements multiple agents (Perception Agent, Safety Agent, Orchestrator) with defined message formats, structured hand‑offs, and full trace logging, satisfying the Tier‑3 requirement for multi‑agent coordination.

Problem & Solution
The Problem
Laboratory environments contain hazards such as open flames, chemicals, and equipment. Human operators may forget PPE (gloves, goggles, lab coats) or unknowingly approach dangerous areas. Manual monitoring is inconsistent and error‑prone.

The Agent
This system perceives lab scenes using YOLO detection, reasons about PPE compliance and hazard proximity using rule‑based logic, and acts by generating annotated images, violation logs, and run summaries. All agent interactions are logged for traceability.

Impact
Lab managers, instructors, and safety officers benefit from automated monitoring that reduces risk, improves compliance, and saves time otherwise spent manually reviewing footage or images.

Agent Architecture
Pipeline:  
Input → Perception (CV tools) → Reasoning → Action → Output

Agent framework: Custom multi‑agent loop with explicit message passing

CV models/tools: YOLOv8 (Ultralytics), custom PPE/hazard classifiers

Reasoning: Rule‑based safety engine (distance thresholds, PPE checks, hazard proximity)

Communication (multi-agent): JSON message schema + orchestrator hand‑off logging

Architecture diagram is available in docs/architecture.md.

Dataset / Test Inputs
Source: Non‑copyrighted lab‑like images (people, PPE, hazards)

Size: 10 sample images included in data/sample/

Classes: person, lab coat, gloves, goggles, open flame, chemical container

Preprocessing: Resize to 640×640, normalization, corrupt image detection

How to Run
Installation
Code
git clone https://github.com/username/Lab-Safety-Multi-Agent-CV-System.git
cd Lab-Safety-Multi-Agent-CV-System
pip install -r requirements.txt
cp .env.example .env   # add API keys only if using LLM reasoning
Quick Start
Place your test images in:

Code
data/input/images/
Run the orchestrator:

Code
python agents/orchestrator.py --image data/sample/test1.jpg
Or run the full batch pipeline:

Code
python agents/orchestrator.py
Outputs appear in:

Code
results/run_YYYYMMDD_HHMMSS/
Evaluation & Results
CV Metrics
Model	Precision	Recall	mAP	Speed (ms/img)
YOLOv8n	~0.75	~0.70	~0.72	~6ms


Agent-Level Metrics
Task success rate: 100% on valid images

Steps per task: 3 (perception → reasoning → action)

Latency: ~0.1–0.2s per image

Success Cases
Annotated images stored in:

Code
results/images/
Failure Cases
Corrupt or unreadable images produce:

Code
*_scene.json (preprocessing_error)
with explanations.

Example Agent Run
A full trace from results/traces/frame_00123_trace.json:

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
Key Learnings
YOLOv8 is fast and reliable for general detection, but PPE detection requires fine‑tuning.

Rule‑based reasoning is simple and transparent, making violations easy to explain.

Multi‑agent orchestration improves modularity and debugging.

Google Colab cannot access webcams; batch image ingestion is the correct approach.

AI Usage
See docs/AI_usage_log.md for detailed attribution and usage notes.

Future Improvements
Add PPE classifier trained on lab-specific images

Add hazard segmentation for more precise detection

Add temporal reasoning (track violations over time)

Add LLM-based reasoning for complex safety policies

Add dashboard UI for real-time monitoring

References
Ultralytics YOLOv8 documentation

OpenCV Python documentation

Course materials from ITAI 1378

License
Academic use only.

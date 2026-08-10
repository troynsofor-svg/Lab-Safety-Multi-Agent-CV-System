# 1. Project Architecture:
1.1 System Overview
The PPE Detection System uses a multi‑agent architecture:

Perception Layer  
YOLOv11 model detects PPE objects and hazards.

Classification Layer

ppe_classifier.py → Determines PPE adherence

hazard_classifier.py → Spots unsafe conditions

Reasoning Layer  
LLM Safety Agent combines detections + classifiers → provides the last safety choice.

Orchestrator Layer  
Organizes the detector, model, and LLM reasoning.

1.2 Repository Structure
Code
project-name/
│
├── README.md
├── requirements.txt
├── .env.example
│
├── agents/
│   ├── perception_agent.py
│   ├── planner_agent.py
│   └── orchestrator.py
│
├── tools/
│   ├── detector.py
│   ├── ppe_classifier.py
│   └── hazard_classifier.py
│
├── prompts/
│   └── system_prompt.txt
│
├── data/
│   ├── sample/
│   └── README.md
│
├── models/
│   ├── best.pt
│   └── last.pt
│
├── notebooks/
│   ├── 
│   ├── 02_evaluation of agents.ipynb
│   
│
├── results/
│   ├── metrics.txt
│   └── traces/
│       ├── trace_001.json
│       ├── trace_002.json
│       ├── trace_003.json
│       └── trace_004.json
│
└── docs/
    ├── architecture.md
    └── AI_usage_log.md

# 2. Setup Instructions
2.1 Clone the Repository
bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>

2.2 Install Dependencies
bash
pip install -r requirements.txt

2.3 Add Environment Variables
Copy .env.example → .env and fill in your API keys.

2.4 Download Model Weights
Place your trained YOLOv11 weights inside:

Code
models/best.pt
models/last.pt
# 3. Usage
3.1 Run Detection
python
from tools.detector import ObjectDetector

detector = ObjectDetector("models/best.pt")
results = detector.detect("image.jpg", save=True)

3.2 PPE Compliance Check
python
from tools.ppe_classifier import PPEClassifier

ppe = PPEClassifier()
ppe_results = ppe.classify(results)
print(ppe_results)

3.3 Hazard Detection
python
from tools.hazard_classifier import HazardClassifier

haz = HazardClassifier()
haz_results = haz.classify(results)
print(haz_results)

3.4 Full Multi‑Agent Reasoning
python
from agents.orchestrator import Orchestrator

orc = Orchestrator()
decision = orc.evaluate("image.jpg")
print(decision)

# 4. Examples
Example Input
Image: test/images/pexels-photo-5726701_avif.jpg

Example Output
json
{
  "ppe_present": ["lab_coat", "gloves", "goggles"],
  "ppe_missing": [],
  "hazards_detected": [],
  "is_compliant": true,
  "hazard_level": "none",
  "final_decision": "SAFE",
  "explanation": "All required PPE detected and no hazards present."
}
# 5. Limitations
The CPU training being super slow:  
YOLOv11 performs better with GPU acceleration.

# Small dataset limitations  
Some PPE categories might have lower recall because of limited samples.

Occlusions decrease accuracy:  
Goggles and gloves might be skipped when they're partially hidden.

Hazard categories depend on dataset quality:  
If hazards are under‑represented, detection might be weaker.

LLM reasoning is deterministic  
It just uses created detections — no external knowledge.

# 6. License
MIT License (or whichever license you as the user can decide)

requirements.txt (Pinned Versions)
Code
ultralytics==8.1.0
opencv-python==4.9.0.80
numpy==1.26.4
torch==2.2.0
torchvision==0.17.0
python-dotenv==1.0.1
pillow==10.2.0
matplotlib==3.8.2
tqdm==4.66.1
These versions are balanced and consistent with YOLOv11.

.env.example
Code
# API Keys (leave blank)
OPENAI_API_KEY=
ANTHROPIC_API_KEY=
AZURE_OPENAI_KEY=
AZURE_OPENAI_ENDPOINT=

# Model configuration
MODEL_NAME=yolo11n

# Optional logging or monitoring keys
WANDB_API_KEY=
This file is safe to commit — it doesn't include no real secrets.

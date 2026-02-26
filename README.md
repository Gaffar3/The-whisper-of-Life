# The-whisper-of-Life markdown
markdown
# Second Pair of Eyes — ICU Early Warning System

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.9+-green)
![Flask](https://img.shields.io/badge/flask-2.3+-lightgrey)
![License](https://img.shields.io/badge/license-MIT-orange)

## 👁️ About the Project

**Second Pair of Eyes** is an early warning system designed to detect patient deterioration in general wards and ICUs. The project was developed for the Harvard Health Systems Innovation Lab Hackathon 2026.

> *"Every week, I see patients brought to us from general wards when it's already too late. This project is a way to give nurses a second pair of eyes."* — Gera, ICU Nurse

### The Problem
In general hospital wards, nurses check on patients during rounds — for example, every 4–6 hours. In between those rounds, a patient's condition can silently deteriorate without visible signs. By the time a nurse notices something wrong — a sudden drop in blood pressure, confusion, or rapid breathing — it is often too late. The patient goes into septic shock or cardiac arrest and is rushed to the ICU with a poor prognosis.

Early detection saves lives. But nurses cannot be in five places at once.

### Our Solution
We built a simple, intelligent tool that works on a tablet or phone. During routine rounds, nurses enter vital signs — heart rate, blood pressure, oxygen saturation, temperature, respiratory rate — into the app. The AI-powered system analyzes trends in real time, trained on thousands of clinical cases to recognize early signs of sepsis, shock, or respiratory failure.

If the system detects a dangerous combination — for example, a 20% drop in blood pressure over two hours with rising heart rate — it sends a **push notification** to the nurse and the on-call doctor:

> **"⚠️ Risk of deterioration — patient in Room 302."**

## 🚀 Quick Start

### Requirements
- Python 3.9 or higher
- pip (package manager)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/second-pair-of-eyes.git
cd second-pair-of-eyes
Install dependencies

bash
pip install -r requirements.txt
Run the application

bash
python app.py
Open in your browser

text
http://localhost:5000
🏗️ Architecture
text
├── app.py                 # Main Flask application
├── models/
│   └── ews_calculator.py  # Risk calculation logic (NEWS2-based)
├── templates/
│   └── index.html         # User interface
├── static/                # CSS and JavaScript files
├── requirements.txt       # Dependencies
└── README.md              # Documentation
Risk Assessment Algorithm
The system uses a modified NEWS2 (National Early Warning Score 2) protocol , adapted for ICU and general ward settings:

Heart Rate (bpm)

Systolic Blood Pressure (mmHg)

Respiratory Rate (breaths/min)

Temperature (°C)

Oxygen Saturation SpO2 (%)

Oxygen Therapy (yes/no)

Level of Consciousness (AVPU scale)

Risk Levels
Score	Risk Level	Color	Recommended Action
0–2	Low	🟢 Green	Routine monitoring
3–4	Medium	🟡 Yellow	Increased observation, reassess in 1 hour
5–6	High	🟠 Orange	Urgent medical review
7+	Critical	🔴 Red	Immediate ICU transfer
🎯 For the Hackathon
Our Team
Gera — 4th-year medical student at Immanuel Kant Baltic Federal University, ICU nurse (Russia)

Denis — Partner, works in ICU (Belarus)

Why Our Approach Stands Out
Real Clinical Experience — We work in ICUs. We see the problem every day.

International Perspective — Russia and Belarus, same challenges, shared mission.

Human-Centered Design — Built for nurses, by people who work alongside them.

Evidence-Based — Algorithm validated against the NEWS2 clinical standard.

Scalable — From small regional hospitals to large medical centers.

Demo Cases
The application includes three pre-loaded clinical scenarios:

✅ Normal — Stable patient, routine monitoring

⚠️ Medium Risk — Warning signs, requires attention

🚨 Critical — Immediate intervention needed

📊 Key Messages for Presentation
The Problem: Delayed detection of deterioration contributes to preventable deaths

Our Solution: AI-assisted early warning system integrated into nursing workflow

The Evidence: Built on validated clinical scoring systems (NEWS2)

Impact: Scalable, low-cost, potentially life-saving

🛠️ Technologies Used
Backend: Python, Flask

Frontend: HTML5, CSS3, JavaScript

Visualization: Plotly

ML/AI: scikit-learn (for advanced version)

📝 License
MIT License — free to use, modify, and distribute

🤝 Contact
For questions or collaboration:

Gera: [geragaffar@mail.ru]

Denis: [den.kulik.05@inbox.ru]

Second Pair of Eyes — Because one pair of eyes cannot always catch everything

Made with ❤️ in Kaliningrad and Minsk for Harvard Health Systems Innovation Lab Hackathon 2026

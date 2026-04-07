# smart-greenhouse-ai🌱 AI-Based Smart Greenhouse Monitoring System

🚀 Overview

This project is an IoT + Machine Learning based smart greenhouse system that monitors environmental conditions and predicts risk levels in real-time.

The system uses ESP32 with multiple sensors and integrates with Blynk Cloud for live monitoring and a Python-based ML model for intelligent decision making.

⸻

⚙️ Features
	•	🌡️ Temperature & Humidity Monitoring (DHT11)
	•	🌫️ Gas / Smoke Detection (MQ Sensor)
	•	🚨 Intrusion Detection (IR Sensor)
	•	⚙️ Automated Ventilation (Servo Motor)
	•	📱 Real-time Dashboard (Blynk IoT)
	•	🧠 Machine Learning Risk Prediction
	•	📊 Live Risk Score Visualization

⸻

🧠 System Architecture

Sensors → ESP32 → Blynk Cloud → Python ML Model → Risk Prediction → Dashboard

⸻

🛠️ Hardware Components
	•	ESP32
	•	DHT11 Sensor
	•	MQ Gas Sensor
	•	IR Sensor
	•	Servo Motor

⸻

💻 Software Stack
	•	Arduino IDE
	•	Python (pandas, scikit-learn)
	•	Blynk IoT Cloud

⸻

📊 Machine Learning
	•	Model: Random Forest Classifier
	•	Inputs: Temperature, Humidity, Gas, Intrusion
	•	Output: Risk Level (Safe / Warning / Danger)

  Project Structure:
esp32_code/
python/
data/
images/

🚀 How to Run

1. Upload ESP32 Code
Use Arduino IDE to upload code to ESP32.

2. Run Data Logger
python python/logger.py

3. Train Model
python python/train_model.py

4. Run Live Prediction
python python/predict_live.py

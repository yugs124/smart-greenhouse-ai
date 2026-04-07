🌱 AI-Powered Smart Greenhouse System (ESP32 + IoT + ML)

A complete end-to-end intelligent greenhouse monitoring and control system using ESP32, Blynk IoT, and Machine Learning.

⸻

🚀 Project Overview

This project combines hardware + cloud + machine learning to create a smart greenhouse system that:
	•	Monitors environmental conditions in real-time
	•	Detects gas, intrusion, and temperature anomalies
	•	Predicts risk levels using a trained ML model
	•	Automatically controls ventilation using a servo motor
	•	Displays live data on a Blynk dashboard

⸻

🧠 System Architecture

Sensors → ESP32 → Blynk Cloud → Python Logger → Dataset → ML Model → Risk Prediction → Dashboard

⸻

⚙️ Features
	•	🌡️ Temperature & Humidity Monitoring (DHT11)
	•	🌫️ Gas Detection (MQ Sensor)
	•	🚨 Intrusion Detection (IR Sensor)
	•	⚙️ Automatic Vent Control (Servo Motor)
	•	📡 Real-time IoT Dashboard (Blynk)
	•	📊 Data Logging (CSV)
	•	🧠 Machine Learning Risk Prediction
	•	📈 Live Risk Score Visualization

⸻

🛠️ Hardware Used
	•	ESP32 Dev Board
	•	DHT11 Sensor
	•	MQ Gas Sensor
	•	IR Sensor
	•	Servo Motor
	•	Breadboard
	•	Jumper Wires

⸻

💻 Software Stack
	•	Arduino IDE
	•	Python
	•	Blynk IoT Cloud

Python Libraries Used
	•	pandas
	•	scikit-learn
	•	requests
	•	joblib

⸻

📁 Project Files

- [esp32-code.ino](./esp32-code.ino) → ESP32 firmware
- [logger.py](./logger.py) → collects real-time data from Blynk
- [train_model.py](./train_model.py) → trains machine learning model
- [live_predictor_file.py](./live_predictor_file.py) → predicts live risk score
- [greenhouse_data_labeled.csv](./greenhouse_data_labeled.csv) → labeled training dataset
- [demo_1.jpeg](./demo_1.jpeg) → dashboard / project image
- [demo_2.jpeg](./demo_2.jpeg) → project image
- [demo_3.jpeg](./demo_3.jpeg) → project setup image

🧠 Machine Learning Details

Model Used:

Random Forest Classifier

Input Features:
	•	Temperature
	•	Humidity
	•	Gas Value
	•	Intrusion Status
	•	Vent Status

Output:
	•	safe
	•	warning
	•	danger

Purpose:

The ML model learns from collected greenhouse data and predicts the risk level of the greenhouse environment in real-time.

⸻

🔌 Working Principle

Step 1 — Sensor Monitoring

The ESP32 continuously reads:
	•	Temperature
	•	Humidity
	•	Gas concentration
	•	Intrusion / movement

⸻

Step 2 — Smart Ventilation

If the environment becomes risky (for example high temperature or gas value), the servo motor rotates to simulate greenhouse vent opening.

⸻

Step 3 — Cloud Monitoring

All sensor data is sent to Blynk Cloud, where it is displayed on a real-time IoT dashboard.

⸻

Step 4 — Data Logging

A Python script (logger.py) fetches this live data from Blynk and stores it into a CSV dataset.

⸻

Step 5 — Machine Learning Training

The collected data is labeled and used to train a machine learning model.

⸻

Step 6 — Live Prediction

Another Python script (live_predictor_file.py) uses the trained model to predict the greenhouse risk level in real-time.

⸻

📈 Example Use Cases

This project can be extended for:
	•	Smart farming
	•	Greenhouse automation
	•	Crop safety monitoring
	•	Industrial environmental monitoring
	•	Hazard detection systems
	•	Smart lab environment monitoring

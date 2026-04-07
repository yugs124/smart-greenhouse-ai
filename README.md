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

Your uploaded files are:
	•	esp32-code.ino → ESP32 firmware
	•	logger.py → collects real-time data from Blynk
	•	train_model.py → trains machine learning model
	•	live_predictor_file.py → predicts live risk score
	•	greenhouse_data_labeled.csv → labeled training dataset
	•	demo_1.jpeg → dashboard / project image
	•	demo_2.jpeg → project image
	•	demo_3.jpeg → project setup image

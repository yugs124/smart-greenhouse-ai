import requests
import joblib
import time
import pandas as pd

# ---------------- SETTINGS ----------------
BLYNK_AUTH_TOKEN = "UhszGK02MjimyYhw4POtiVNXHxl_RgAj"

# ---------------- LOAD TRAINED MODEL ----------------
model = joblib.load("greenhouse_model.pkl")

print("Live AI prediction started... Press Ctrl+C to stop.")
print("Model classes:", model.classes_)

while True:
    try:
        # ---------------- READ CURRENT VALUES FROM BLYNK ----------------
        temp = float(requests.get(f"https://blynk.cloud/external/api/get?token={BLYNK_AUTH_TOKEN}&V0").text)
        humidity = float(requests.get(f"https://blynk.cloud/external/api/get?token={BLYNK_AUTH_TOKEN}&V1").text)
        gas = int(float(requests.get(f"https://blynk.cloud/external/api/get?token={BLYNK_AUTH_TOKEN}&V2").text))
        intrusion = int(float(requests.get(f"https://blynk.cloud/external/api/get?token={BLYNK_AUTH_TOKEN}&V3").text))

        # ---------------- PREPARE INPUT ----------------
        input_data = pd.DataFrame([{
            "temp": temp,
            "humidity": humidity,
            "gas": gas,
            "intrusion": intrusion
        }])

        # ---------------- PREDICT LABEL ----------------
        prediction = model.predict(input_data)[0]
        prediction = str(prediction).strip().lower()

        # ---------------- CONVERT LABEL TO RISK SCORE ----------------
        if prediction == "safe":
            risk_score = 20
        elif prediction == "warning":
            risk_score = 60
        elif prediction == "danger":
            risk_score = 95
        else:
            risk_score = 0

        # ---------------- SEND TO BLYNK V5 ----------------
        requests.get(
            f"https://blynk.cloud/external/api/update?token={BLYNK_AUTH_TOKEN}&V5={risk_score}"
        )

        print("====================================")
        print(f"Temp       : {temp}")
        print(f"Humidity   : {humidity}")
        print(f"Gas        : {gas}")
        print(f"Intrusion  : {intrusion}")
        print(f"Prediction : {prediction}")
        print(f"Risk Score : {risk_score}")

        time.sleep(5)

    except Exception as e:
        print("Error:", e)
        time.sleep(5)
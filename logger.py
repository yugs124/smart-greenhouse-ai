import requests
import pandas as pd
import os
import time
from datetime import datetime

# ---------------- BLYNK SETTINGS ----------------
BLYNK_AUTH_TOKEN = "UhszGK02MjimyYhw4POtiVNXHxl_RgAj"

# ---------------- CSV FILE ----------------
csv_file = "greenhouse_data.csv"

# ---------------- CREATE FILE IF NOT EXISTS ----------------
if not os.path.exists(csv_file):
    df = pd.DataFrame(columns=[
        "timestamp", "temp", "humidity", "gas", "intrusion", "vent_status"
    ])
    df.to_csv(csv_file, index=False)

print("Logging started... Press Ctrl+C to stop.")

while True:
    try:
        temp = requests.get(f"https://blynk.cloud/external/api/get?token={BLYNK_AUTH_TOKEN}&V0").text
        humidity = requests.get(f"https://blynk.cloud/external/api/get?token={BLYNK_AUTH_TOKEN}&V1").text
        gas = requests.get(f"https://blynk.cloud/external/api/get?token={BLYNK_AUTH_TOKEN}&V2").text
        intrusion = requests.get(f"https://blynk.cloud/external/api/get?token={BLYNK_AUTH_TOKEN}&V3").text
        vent_status = requests.get(f"https://blynk.cloud/external/api/get?token={BLYNK_AUTH_TOKEN}&V4").text

        row = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "temp": float(temp),
            "humidity": float(humidity),
            "gas": int(float(gas)),
            "intrusion": int(float(intrusion)),
            "vent_status": int(float(vent_status))
        }

        pd.DataFrame([row]).to_csv(csv_file, mode='a', header=False, index=False)

        print("Logged:", row)
        time.sleep(5)

    except Exception as e:
        print("Error:", e)
        time.sleep(5)
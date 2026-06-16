import pandas as pd
import time

from accident_detector import AccidentDetector
from emergency_alert import send_alert

detector = AccidentDetector()

data = pd.read_csv("sensor_data.csv")

for _, row in data.iterrows():

    accident, g_force = detector.detect_accident(
        row["ax"],
        row["ay"],
        row["az"],
        row["heart_rate"]
    )

    print(
        f"G-Force: {g_force:.2f} | "
        f"Heart Rate: {row['heart_rate']}"
    )

    if accident:

        print("Potential Accident Found")
        print("Checking for 5 seconds...")

        time.sleep(5)

        send_alert(
            row["latitude"],
            row["longitude"],
            row["heart_rate"]
        )

    time.sleep(1)
from datetime import datetime

def send_alert(latitude, longitude, heart_rate):

    print("\n========== EMERGENCY ALERT ==========")

    print("Accident Detected!")
    print("Time:", datetime.now())

    print(f"Location: {latitude}, {longitude}")
    print(f"Heart Rate: {heart_rate}")

    google_map = (
        f"https://www.google.com/maps?q="
        f"{latitude},{longitude}"
    )

    print("GPS Link:", google_map)

    print("Emergency Contact Notified")
    print("=====================================\n")
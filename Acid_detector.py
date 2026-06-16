import math

class AccidentDetector:

    def __init__(self):
        self.impact_threshold = 4.0  # 4G threshold

    def calculate_g_force(self, ax, ay, az):
        return math.sqrt(ax**2 + ay**2 + az**2)

    def detect_accident(self, ax, ay, az, heart_rate):

        g_force = self.calculate_g_force(ax, ay, az)

        if g_force > self.impact_threshold:
            if heart_rate > 110 or heart_rate < 50:
                return True, g_force

        return False, g_force
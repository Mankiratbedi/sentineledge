import time
import random

class SentinelAgent:
    def __init__(self):
        self.status = "IDLE"
        self.risk_score = 0.0
    
    def observe(self):
        """Simulates 'Observe': Reading frames."""
        self.status = "OBSERVING"
        return True

    def orient(self, frame_quality="High"):
        """Simulates 'Orient': Checking compression/quality."""
        self.status = "ORIENTING"
        time.sleep(0.1)
        return "MobileNetV3_Int8"

    def decide(self):
        """Simulates 'Decide': Running Inference."""
        self.status = "ANALYZING"
        
        visual_confidence = random.uniform(0.1, 0.9)
        audio_confidence = random.uniform(0.1, 0.9)
        
        final_score = (visual_confidence * 0.7) + (audio_confidence * 0.3)
        self.risk_score = final_score
        return final_score

    def act(self, score):
        """Simulates 'Act': Triggering Alerts."""
        if score > 0.75:
            return "🔴 THREAT DETECTED: Deepfake Signature Found"
        elif score > 0.4:
            return "🟡 WARNING: Potential Artifacts"
        else:
            return "🟢 CLEAR: Media Authenticated"
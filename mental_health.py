import random

class MentalHealthCompanion:
    def __init__(self, user_name):
        self.user_name = user_name

    def breathing_exercise(self):
        return "Follow this breathing exercise: Inhale for 4 seconds, hold for 7 seconds, exhale for 8 seconds."

    def mood_check_in(self):
        moods = ["happy", "sad", "stressed", "calm"]
        return f"How are you feeling today? You seem {random.choice(moods)}."

    def daily_tip(self):
        tips = [
            "Take a walk in nature to clear your mind.",
            "Write down three things you're grateful for.",
            "Spend time with loved ones."
        ]
        return f"Daily tip: {random.choice(tips)}"
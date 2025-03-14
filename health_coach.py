import random

class HealthCoach:
    def __init__(self, user_name):
        self.user_name = user_name
        self.steps = 0
        self.water_intake = 0

    def track_steps(self, steps):
        self.steps += steps
        return f"Steps tracked! Total steps today: {self.steps}"

    def track_water(self, amount):
        self.water_intake += amount
        return f"Water intake tracked! Total water today: {self.water_intake} ml"

    def suggest_workout(self):
        workouts = ["10 push-ups", "15 squats", "5-minute plank", "20 jumping jacks"]
        return f"Suggested workout: {random.choice(workouts)}"

    def suggest_meal(self, dietary_preference):
        meals = {
            "vegetarian": ["Vegetable stir-fry", "Quinoa salad", "Lentil soup"],
            "non-vegetarian": ["Grilled chicken with veggies", "Salmon with rice", "Egg omelette"],
            "vegan": ["Tofu curry", "Chickpea salad", "Avocado toast"]
        }
        return f"Suggested meal: {random.choice(meals[dietary_preference])}"
from geopy.geocoders import Nominatim

class EmergencyHelper:
    def __init__(self):
        self.geolocator = Nominatim(user_agent="emergency_helper")

    def first_aid_steps(self, emergency_type):
        steps = {
            "accident": "1. Call 911. 2. Check for injuries. 3. Do not move the injured person.",
            "fire": "1. Evacuate immediately. 2. Call 911. 3. Use a fire extinguisher if safe.",
            "earthquake": "1. Drop, cover, and hold on. 2. Stay indoors. 3. Avoid windows."
        }
        return steps.get(emergency_type, "No steps available for this emergency.")

    def locate_nearby_help(self, location):
        try:
            location = self.geolocator.geocode(location)
            return f"Nearby hospitals and pharmacies can be found at: {location.address}"
        except:
            return "Unable to locate nearby help."
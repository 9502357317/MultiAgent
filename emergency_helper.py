import requests
from geopy.geocoders import Nominatim

class EmergencyHelper:
    def __init__(self):
        self.geolocator = Nominatim(user_agent="emergency_helper")
        self.first_aid_api_url = "https://www.firstaidapi.com/api/"

    def first_aid_steps(self, emergency_type):
        """
        Fetch first-aid steps for a specific emergency type using the First Aid API.
        If the API fails, use hardcoded steps as a fallback.
        """
        # Hardcoded first-aid steps as a fallback
        hardcoded_steps = {
            "accident": "1. Call 108. 2. Check for injuries. 3. Do not move the injured person.",
            "fire": "1. Evacuate immediately. 2. Call 108. 3. Use a fire extinguisher if safe.",
            "earthquake": "1. Drop, cover, and hold on. 2. Stay indoors. 3. Avoid windows.",
            "burn": "1. Cool the burn under cool running water for at least 10 minutes. 2. Remove any clothing or jewelry near the burn, unless stuck to the skin. 3. Cover the burn with a sterile dressing or clean cloth. 4. Do not apply creams, ointments, or ice to the burn. 5. Seek medical attention if the burn is severe.",
            "cut": "1. Apply pressure to the wound with a clean cloth to stop bleeding. 2. Clean the wound with water. 3. Apply an antibiotic ointment. 4. Cover the wound with a bandage. 5. Seek medical attention if the cut is deep or bleeding does not stop.",
            "choking": "1. Perform the Heimlich maneuver. 2. Call 108 if the person cannot breathe, cough, or speak. 3. Continue abdominal thrusts until the object is dislodged or medical help arrives."
        }

        try:
            # Try fetching first-aid instructions from the API
            response = requests.get(f"{self.first_aid_api_url}?id={emergency_type}")
            if response.status_code == 200:
                data = response.json()
                return data.get("instructions", hardcoded_steps.get(emergency_type, "No instructions available for this emergency."))
            else:
                # If the API fails, use hardcoded steps
                return hardcoded_steps.get(emergency_type, "No instructions available for this emergency.")
        except Exception as e:
            # If an error occurs, use hardcoded steps
            return hardcoded_steps.get(emergency_type, f"An error occurred: {str(e)}")

    def locate_nearby_help(self, location):
        """
        Locate nearby hospitals or pharmacies using Geopy.
        """
        try:
            location = self.geolocator.geocode(location)
            if location:
                return f"Nearby hospitals and pharmacies can be found at: {location.address}"
            else:
                return "Unable to locate nearby help. Please check your location input."
        except Exception as e:
            return f"An error occurred: {str(e)}"

    def send_alert(self, contacts):
        """
        Simulate sending an emergency alert to contacts.
        """
        return f"Emergency alert sent to: {', '.join(contacts)}"

# Example usage
if __name__ == "__main__":
    helper = EmergencyHelper()

    # Fetch first-aid steps for a burn injury
    emergency_type = "burn"  # Example: burn, cut, choking, etc.
    print("First Aid Steps:")
    print(helper.first_aid_steps(emergency_type))

    # Locate nearby help
    location = "New York"
    print("\nNearby Help:")
    print(helper.locate_nearby_help(location))

    # Send emergency alert
    contacts = ["contact1@example.com", "contact2@example.com"]
    print("\nEmergency Alert:")
    print(helper.send_alert(contacts))
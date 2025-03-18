import requests

class WeatherAdvisor:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, city):
        """
        Fetch weather data for a given city using OpenWeatherMap API.
        """
        try:
            response = requests.get(f"{self.base_url}?q={city}&appid={self.api_key}&units=metric")
            if response.status_code == 200:
                return response.json()
            else:
                return None
        except Exception as e:
            return f"An error occurred: {str(e)}"

    def get_clothing_advice(self, city):
        """
        Provide clothing advice based on the current weather in the given city.
        """
        weather_data = self.get_weather(city)
        if not weather_data or "main" not in weather_data:
            return "Unable to fetch weather data. Please check the city name or try again later."

        temperature = weather_data["main"]["temp"]
        weather_condition = weather_data["weather"][0]["main"].lower()

        # Clothing advice based on temperature and weather condition
        if temperature < 10:
            advice = "It's very cold! Wear a heavy coat, scarf, gloves, and a hat."
        elif 10 <= temperature < 20:
            advice = "It's chilly. Wear a jacket or sweater."
        elif 20 <= temperature < 30:
            advice = "It's warm. Wear light clothing like a t-shirt and jeans."
        else:
            advice = "It's hot! Wear light and breathable clothing like shorts and a t-shirt."

        # Additional advice based on weather condition
        if "rain" in weather_condition:
            advice += " Don't forget an umbrella or raincoat!"
        elif "snow" in weather_condition:
            advice += " Wear waterproof boots and stay warm!"
        elif "clear" in weather_condition:
            advice += " Enjoy the sunny weather!"

        return advice
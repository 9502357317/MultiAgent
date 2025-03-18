import streamlit as st
from health_coach import HealthCoach
from translator import LanguageTranslator
from emergency_helper import EmergencyHelper
from mental_health import MentalHealthCompanion
from weather_advisor import WeatherAdvisor

# Initialize helpers
helper = EmergencyHelper()
translator = LanguageTranslator()
weather_advisor = WeatherAdvisor(api_key="64525c93e5407951bace3eb1f87425ec")  # Replace with your API key

# App title and welcome message
st.title("AI Agent: Your Personal Assistant")
st.write("Welcome to the AI Agent! Use the sidebar to navigate between features.")

# Sidebar navigation
st.sidebar.title("Navigation")
choice = st.sidebar.radio(
    "Choose a module",
    [
        "Health and Wellness Coach",
        "Language Translator",
        "Emergency Helper",
        "Mental Health Companion",
        "Weather Advisor",
    ],
    help="Select a module to get started."
)

# Health and Wellness Coach
if choice == "Health and Wellness Coach":
    st.header("Health and Wellness Coach")
    user_name = st.text_input("Enter your name:")
    if user_name:
        coach = HealthCoach(user_name)
        st.write(coach.track_steps(1000))
        st.write(coach.track_water(500))
        st.write(coach.suggest_workout())
        dietary_preference = st.selectbox("Select your dietary preference", ["vegetarian", "non-vegetarian", "vegan"])
        st.write(coach.suggest_meal(dietary_preference))

# Language Translator
if choice == "Language Translator":
    st.header("Language Translator")
    text = st.text_input("Enter text to translate:")
    language = st.text_input("Enter target language (e.g., 'es' for Spanish):")
    if text and language:
        translated_text = translator.translate_text(text, language)
        st.write(f"Translated Text: {translated_text}")
        if st.button("Speak Translation"):
            translator.speak_text(translated_text, language)

# Emergency Helper
if choice == "Emergency Helper":
    st.header("Emergency Helper")
    emergency_type = st.selectbox(
        "Select emergency type",
        ["accident", "fire", "earthquake", "burn", "cut", "choking"],
        help="Choose the type of emergency."
    )
    if emergency_type:
        steps = helper.first_aid_steps(emergency_type)
        st.write("First Aid Steps:")
        st.write(steps)

    location = st.text_input("Enter your location (e.g., New York):")
    if location:
        nearby_help = helper.locate_nearby_help(location)
        st.write(nearby_help)

        # Display a map (example coordinates)
        st.map({
            "latitude": [40.7128],  # Example latitude for New York
            "longitude": [-74.0060]  # Example longitude for New York
        })

# Mental Health Companion
if choice == "Mental Health Companion":
    st.header("Mental Health Companion")
    user_name = st.text_input("Enter your name:")
    if user_name:
        companion = MentalHealthCompanion(user_name)
        st.write(companion.breathing_exercise())
        st.write(companion.mood_check_in())
        st.write(companion.daily_tip())

# Weather Advisor
if choice == "Weather Advisor":
    st.header("Weather Advisor")
    city = st.text_input("Enter your city:")
    if city:
        advice = weather_advisor.get_clothing_advice(city)
        st.write("Clothing Advice:")
        st.write(advice)

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("Built with ❤️ by [Your Name](https://github.com/9502357317)")
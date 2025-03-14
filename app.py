import streamlit as st
from health_coach import HealthCoach
from translator import LanguageTranslator
from emergency_helper import EmergencyHelper
from mental_health import MentalHealthCompanion

# Page Title
st.title("AI Agent: Your Personal Assistant")

# Sidebar Navigation
st.sidebar.title("Navigation")
choice = st.sidebar.radio("Choose a module", [
    "Health and Wellness Coach",
    "Language Translator",
    "Emergency Helper",
    "Mental Health Companion"
])

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
elif choice == "Language Translator":
    st.header("Language Translator")
    text = st.text_input("Enter text to translate:")
    language = st.text_input("Enter target language (e.g., 'es' for Spanish):")
    if text and language:
        translator = LanguageTranslator()
        translated_text = translator.translate_text(text, language)
        st.write(f"Translated Text: {translated_text}")
        if st.button("Speak Translation"):
            translator.speak_text(translated_text, language)

# Emergency Helper
elif choice == "Emergency Helper":
    st.header("Emergency Helper")
    emergency_type = st.selectbox("Select emergency type", ["accident", "fire", "earthquake"])
    location = st.text_input("Enter your location:")
    if emergency_type and location:
        helper = EmergencyHelper()
        st.write(helper.first_aid_steps(emergency_type))
        st.write(helper.locate_nearby_help(location))

# Mental Health Companion
elif choice == "Mental Health Companion":
    st.header("Mental Health Companion")
    user_name = st.text_input("Enter your name:")
    if user_name:
        companion = MentalHealthCompanion(user_name)
        st.write(companion.breathing_exercise())
        st.write(companion.mood_check_in())
        st.write(companion.daily_tip())
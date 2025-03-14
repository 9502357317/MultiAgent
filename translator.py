from googletrans import Translator
from gtts import gTTS
import playsound
import os

class LanguageTranslator:
    def __init__(self):
        self.translator = Translator()

    def translate_text(self, text, dest_language):
        translation = self.translator.translate(text, dest=dest_language)
        return translation.text

    def speak_text(self, text, language):
        tts = gTTS(text=text, lang=language)
        tts.save("output.mp3")
        playsound.playsound("output.mp3")
        os.remove("output.mp3")

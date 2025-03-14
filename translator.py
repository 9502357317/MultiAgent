from translate import Translator

class LanguageTranslator:
    def __init__(self):
        self.translator = Translator(to_lang="es")  # Default target language

    def translate_text(self, text, dest_language):
        self.translator = Translator(to_lang=dest_language)
        translation = self.translator.translate(text)
        return translation

    def speak_text(self, text, language):
        from gtts import gTTS
        import playsound
        import os
        tts = gTTS(text=text, lang=language)
        tts.save("output.mp3")
        playsound.playsound("output.mp3")
        os.remove("output.mp3")
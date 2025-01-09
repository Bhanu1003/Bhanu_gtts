from gtts import gTTS
from googletrans import Translator

# Set up text and target language
text = "Chiru is Bokada"
target_language = "kn"  # Telugu language code

# Translate the text
translator = Translator()
translation = translator.translate(text, dest=target_language)
translated_text = translation.text
print("Translated Text:", translated_text)

# Convert the translated text to speech
speech = gTTS(text=translated_text, lang=target_language, slow=False)
speech.save("auto_translate.mp3")

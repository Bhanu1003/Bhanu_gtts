from gtts import gTTS
language = "kn"

text = "ಹಲೋ ವಿಕ್ರಮ್, ದಯವಿಟ್ಟು ನನ್ನ ಉಚ್ಚಾರಣೆಯನ್ನು ಒಮ್ಮೆ ಪರೀಕ್ಷಿಸಬಹುದೇ?"

speech = gTTS(text=text, lang= language, tld="com.au")
speech.save("op.mp3")

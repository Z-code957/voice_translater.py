import speech_recognition as sr
import pyttsx3
from googletrans import Translator

# Initialize Text-to-Speech engine once
engine = pyttsx3.init()
engine.setProperty("rate", 150)


def speak(text):
    """Speak the translated text."""
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print("Error while speaking:", e)


def speech_to_text():
    """Convert spoken English into text."""
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("\nListening... Please speak in English.")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio, language="en-US")
        print("You said:", text)
        return text

    except sr.UnknownValueError:
        print("Sorry, I couldn't understand your speech.")
        return ""

    except sr.RequestError as e:
        print("Speech Recognition service error:", e)
        return ""


def translate_text(text, target_language):
    """Translate text into the selected language."""
    try:
        translator = Translator()
        translated = translator.translate(text, dest=target_language)

        print("\nTranslated Text:")
        print(translated.text)

        return translated.text

    except Exception as e:
        print("Translation Error:", e)
        return ""


def display_language_options():
    """Display available translation languages."""
    languages = {
        "1": ("Hindi", "hi"),
        "2": ("Tamil", "ta"),
        "3": ("Telugu", "te"),
        "4": ("Bengali", "bn"),
        "5": ("Marathi", "mr"),
        "6": ("Gujarati", "gu"),
        "7": ("Malayalam", "ml"),
        "8": ("Punjabi", "pa")
    }

    print("\n====== Language Options ======")

    for key, value in languages.items():
        print(f"{key}. {value[0]}")

    choice = input("\nEnter your choice (1-8): ")

    if choice in languages:
        return languages[choice][1]
    else:
        print("Invalid choice! Defaulting to Hindi.")
        return "hi"


def main():
    print("===================================")
    print(" Speech Translation Application")
    print("===================================")

    target_language = display_language_options()

    original_text = speech_to_text()

    if original_text:
        translated_text = translate_text(original_text, target_language)

        if translated_text:
            speak(translated_text)
            print("\nTranslation spoken successfully!")
    else:
        print("No speech detected.")


if __name__ == "__main__":
    main()
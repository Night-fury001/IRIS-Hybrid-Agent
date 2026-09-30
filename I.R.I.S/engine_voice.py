# --- This file is responsible for converting text into spoken audio using the local system voice engine. ---
import pyttsx3

# --- Speak a given text aloud using the Windows text-to-speech engine. ---
def speak(text):
    # --- Ignore empty strings to prevent errors. ---
    if not text:
        return
    try:
        # --- Create a new speech engine each time so Windows does not block repeated calls. ---
        engine = pyttsx3.init()

        # --- Set the speaking speed and choose a voice that sounds clear and natural. ---
        engine.setProperty('rate', 175)
        voices = engine.getProperty('voices')
        if len(voices) > 1:
            engine.setProperty('voice', voices[1].id)
        else:
            engine.setProperty('voice', voices[0].id)

        # --- Tell the engine what to say and wait until it finishes speaking. ---
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        # --- If the voice engine fails, print the problem so the app can continue. ---
        print(f"[Voice Error]: {e}")
# --- This file is the main voice assistant loop. It listens for the wake word "IRIS" and then waits for a command. ---
import speech_recognition as sr
import time
import sys
from processedCommand import processedCommand
from engine_voice import speak

# --- Create the speech recognizer object used to listen to microphone input. ---
recognizer = sr.Recognizer()

# --- Adjust the microphone behavior so that short pauses between words are handled naturally. ---
recognizer.pause_threshold = 1.2
recognizer.non_speaking_duration = 0.5

# --- Run the assistant when this script is started directly. ---
if __name__ == "__main__":
    # --- Announce the wake word and begin microphone setup. ---
    speak("Say IRIS to activate")
    print("\n[System Initialization] Calibrating microphone for background noise... Please wait.")

    # --- Listen once to the microphone and reduce background noise for better recognition. ---
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.4)

    print("[System Running] Waiting silently for you to say 'IRIS'...")

    # --- Keep the assistant running forever and listen in a loop. ---
    while True:
        try:
            # --- Wait for any sound around the microphone. If nothing is heard for 3 seconds, try again. ---
            with sr.Microphone() as source:
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=4)

            # --- Turn the audio into text and lower it for comparison. ---
            word = recognizer.recognize_google(audio).lower()
            print(f"Background heard: {word}")

            # --- Check whether the wake word "IRIS" was spoken. ---
            if "iris" in word:
                # --- Remove the wake word and check whether the remaining text looks like a real command. ---
                fast_command = word.replace("iris", "").strip()
                valid_triggers = ["open", "play", "deactivate", "how", "who", "launch", "check"]
                is_real_command = any(trigger in fast_command for trigger in valid_triggers)

                # --- If the user says a valid action right after the wake word, run it immediately. ---
                if fast_command and is_real_command:
                    processedCommand(fast_command)
                    print("\n[System Running] Waiting silently for you to say 'IRIS'...")
                    continue

                # --- If the user only said the wake word, the assistant asks for a command. ---
                speak("Yes sir, I am listening. how can I assist you?")
                print(f"---> IRIS responded: Yes sir, I am listening. how can I assist you?")

                # --- Enter the active listening mode until the user gives a command or stops speaking. ---
                while True:
                    print("\n>>> IRIS IS AWAKE! Listening for your command now...")
                    try:
                        # --- Listen for a full command using a longer timeout. ---
                        with sr.Microphone() as source:
                            cmd_audio = recognizer.listen(source, timeout=8, phrase_time_limit=10)

                        command = recognizer.recognize_google(cmd_audio).lower()
                        print(f"You commanded: {command}")

                        # --- Remove the wake word from any command and ignore empty text. ---
                        clean_command = command.replace("iris", "").strip()

                        if not clean_command:
                            print("[System]: Empty command ignored. Waiting for instruction...")
                            continue

                        # --- If the user says deactivate, shut the assistant down cleanly. ---
                        if "deactivate" in clean_command:
                            speak("Deactivating IRIS. Have a nice day, sir.")
                            print(f"---> IRIS responded: Deactivating IRIS. Have a nice day, sir.")
                            print("\n[System Shutting Down]")
                            sys.exit(0)
                        else:
                            # --- Send the command to the action router for processing. ---
                            processedCommand(clean_command)
                            print("\n[System Running] Waiting silently for you to say 'IRIS'...")
                            break

                    except sr.WaitTimeoutError:
                        print("[Timed out]: Didn't hear a command in time. Going back to sleep...")
                        break
                    except sr.UnknownValueError:
                        print("[Unclear]: Could not understand command. Asking to repeat...")
                        speak("I didn't catch that. Please repeat your command.")

        except sr.WaitTimeoutError:
            # --- No voice was detected for a while, so continue listening silently. ---
            continue
        except sr.UnknownValueError:
            # --- Ignore unclear sounds and keep waiting for a valid wake word. ---
            continue
        except Exception as e:
            # --- Catch unexpected microphone problems and keep the system stable. ---
            print(f"[Microphone Error]: {e}")
            time.sleep(0.5)
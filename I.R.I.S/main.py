import speech_recognition as sr
import time
from processedCommand import processedCommand, speak
import sys

recognizer = sr.Recognizer()

if __name__ == "__main__":
    # --- SYSTEM INITIALIZATION ---
    speak("Say IRIS to activate")
    print("\n[System Initialization] Calibrating microphone for background noise... Please wait.")
    
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=2)
        
    print("[System Running] Waiting silently for you to say 'IRIS'...")

    while True:
        try:
            # --- LISTEN FOR WAKE WORD ---
            with sr.Microphone() as source:
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=3)

            word = recognizer.recognize_google(audio).lower()
            print(f"Background heard: {word}")

            # --- Check for wake word "IRIS" ---
            if "iris" in word:
                
                # --- Check for fast command after wake word ---
                fast_command = word.replace("iris", "").strip()
                
                # --- Check if fast command contains valid triggers (Updated to include system commands) ---
                valid_triggers = ["open", "play", "deactivate", "how", "who", "launch", "check"]
                is_real_command = any(trigger in fast_command for trigger in valid_triggers)

                if fast_command and is_real_command:
                    processedCommand(fast_command)
                    print("\n[System Running] Waiting silently for you to say 'IRIS'...")
                    continue

                speak("Yes sir, I am listening. how can I assist you?")
                print(f"---> IRIS responded: Yes sir, I am listening. how can I assist you?")
                
                # --- LISTEN FOR COMMAND ---
                while True:
                    print("\n>>> IRIS IS AWAKE! Listening for your command now...")
                    try:
                        with sr.Microphone() as source:
                            cmd_audio = recognizer.listen(source, timeout=7, phrase_time_limit=5)

                        command = recognizer.recognize_google(cmd_audio).lower()
                        print(f"You commanded: {command}")

                        #--- Check for deactivation command ---
                        if "deactivate" in command:
                            speak("Deactivating IRIS. Have a nice day, sir.")
                            print(f"---> IRIS responded: Deactivating IRIS. Have a nice day, sir.")
                            print("\n[System Shutting Down]")
                            sys.exit(0)
                        else:
                            #--- PROCESS COMMAND ---
                            processedCommand(command)
                            print("\n[System Running] Waiting silently for you to say 'IRIS'...")
                            break

                    except sr.WaitTimeoutError:
                        print("[Timed out]: Didn't hear a command in time. Going back to sleep...")
                        break
                        
                    except sr.UnknownValueError:
                        print("[Unclear]: Could not understand command. Asking to repeat...")
                        speak("I didn't catch that. Please repeat your command.")
                        print(f"---> IRIS responded: I didn't catch that. Please repeat your command.")

        except sr.WaitTimeoutError:
            continue
        except sr.UnknownValueError:
            continue
        except Exception as e:
            print(f"[Microphone Error]: {e}")
            time.sleep(1)
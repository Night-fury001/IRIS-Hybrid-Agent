# --- This file decides what an understood voice command should do. It sends the command to the local AI, reads the action, and calls the correct function. ---
from engine_voice import speak
from engine_llm import get_intent
from engine_actions import open_website, play_music, launch_vscode, check_hardware

# --- Process a command by asking the local AI what action should be taken. ---
def processedCommand(command):
    # --- Show the raw command in the console for debugging and transparency. ---
    print(f"\nProcessing command through local LLM: {command}")

    # --- Ask the AI model to classify the user's request into a structured action. ---
    intent = get_intent(command)
    print(f"LLM Output: {intent}")

    # --- Read the important pieces from the AI response. ---
    action = intent.get("action")
    target = intent.get("target")
    reply = intent.get("reply")

    # --- Route the command to the correct behavior based on the action returned by the model. ---
    if action == "open_website" and target:
        # --- Open a website such as Google, YouTube, or GitHub. ---
        msg = f"Opening {target}."
        print(f"---> IRIS: {msg}")
        speak(msg)
        open_website(target)

    elif action == "play_music":
        # --- Play music or a YouTube video using the given target text. ---
        msg = f"Playing {target}." if target else "Opening YouTube."
        print(f"---> IRIS: {msg}")
        speak(msg)
        play_music(target)

    elif action == "launch_vscode":
        # --- Open Visual Studio Code when the user asks to launch the editor. ---
        msg = "Launching Visual Studio Code."
        print(f"---> IRIS: {msg}")
        speak(msg)
        launch_vscode()

    elif action == "check_hardware":
        # --- Show system hardware information such as GPU stats. ---
        msg = "Checking system hardware details."
        print(f"---> IRIS: {msg}")
        speak(msg)
        check_hardware()

    elif action == "chat":
        # --- Handle general conversation using the AI-generated reply text. ---
        if reply:
            print(f"---> IRIS responded: {reply}")
            speak(reply)

    else:
        # --- If the AI does not understand the request, use a safe fallback message. ---
        fallback_msg = reply if reply else "I am not sure how to handle that request, sir."
        speak(fallback_msg)
        print(f"---> Unknown action. Fallback: {fallback_msg}")
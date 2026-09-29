from engine_voice import speak
from engine_llm import get_intent
from engine_actions import open_website, play_music

def processedCommand(command):
    print(f"\nProcessing command through local LLM: {command}")
    
    intent = get_intent(command)
    print(f"LLM Output: {intent}")
    
    action = intent.get("action")
    target = intent.get("target")
    reply = intent.get("reply")

    if action == "open_website" and target:
        open_website(target)

    elif action == "play_music" and target:
        play_music(target)

    elif action == "chat" and reply:
        print(f"---> IRIS responded: {reply}")
        speak(reply)

    else:
        fallback_msg = reply if reply else "I am not sure how to handle that request, sir."
        speak(fallback_msg)
        print(f"---> Unknown action. LLM Reply: {fallback_msg}")
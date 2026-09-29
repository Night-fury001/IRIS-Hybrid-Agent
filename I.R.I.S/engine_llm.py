import requests
import json

def get_intent(command):
    system_prompt = """You are the core logic router for an AI assistant named IRIS.
    Analyze the user's command and return ONLY a strict JSON object. Do not include markdown formatting, conversational text, or explanations. 

    Valid "action" values:
    - "open_website" (User wants to open a site like GitHub, LeetCode, YouTube, etc.)
    - "play_music" (User wants to play a song or video)
    - "chat" (General questions, greetings, or small talk)
    - "unknown" (Unrecognized or ambiguous commands)

    JSON Schema to follow exactly:
    {"action": "string", "target": "string or null", "reply": "string or null"}
    """

    payload = {
        "model": "phi3.5", 
        "prompt": f"{system_prompt}\n\nUser command: '{command}'",
        "stream": False,
        "format": "json"
    }

    try:
        response = requests.post("http://localhost:11434/api/generate", json=payload)
        response_data = response.json()
        return json.loads(response_data["response"])
        
    except requests.exceptions.ConnectionError:
        print("[Error]: Ollama is not running.")
        return {"action": "unknown", "target": None, "reply": "My neural network is currently offline."}
    except json.JSONDecodeError:
        print("[Error]: LLM failed to return valid JSON.")
        return {"action": "unknown", "target": None, "reply": "I encountered an error processing your logic."}
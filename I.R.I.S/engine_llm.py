# --- This file connects the voice assistant to the local AI model and turns raw commands into structured JSON actions. ---
import requests
import json
import ast
import re
from engine_server import start_local_ai_background

# --- Extract a JSON or Python dictionary from the AI response and convert it into a real Python dictionary. ---
def extract_and_parse(text):
    """Safely parse JSON or Python dict formats from raw text."""
    # --- Find the first dictionary-like structure in the returned text. ---
    match = re.search(r'\{.*\}', text, re.DOTALL)
    if match:
        dict_str = match.group(0).strip()
    else:
        dict_str = text.strip()

    # --- Try standard JSON parsing first. ---
    try:
        return json.loads(dict_str)
    except Exception:
        pass

    # --- If the AI returns Python-style dict syntax, parse it safely. ---
    try:
        parsed = ast.literal_eval(dict_str)
        if isinstance(parsed, dict):
            return parsed
    except Exception:
        pass

    # --- If it is not valid dictionary text, raise a clear error. ---
    raise ValueError(f"Could not parse valid dictionary from: {dict_str}")

# --- Ask the local AI model to classify the spoken command and return an action dictionary. ---
def get_intent(command):
    # --- Make sure the local AI server is running before sending a request. ---
    start_local_ai_background()

    # --- This prompt tells the model exactly how to format its answer. ---
    system_prompt = """You are a strict JSON command router for an OS assistant named IRIS.
Convert the user's spoken command into an executable action. Never act as a conversational bot or explain words. Always output valid JSON only.

Supported actions:
- "open_website": For opening sites (target = site name or domain, e.g. "youtube", "google", "github", "leetcode")
- "play_music": For playing songs, videos, or music (target = song/video query, e.g. "kya baat hai")
- "launch_vscode": For opening code editor or IDE (target = null)
- "check_hardware": For GPU, CPU, RAM, or system stats (target = null)
- "chat": For general questions and small talk (target = null)

Examples:
Command: "open youtube" -> {"action": "open_website", "target": "youtube", "reply": "Opening YouTube."}
Command: "open google" -> {"action": "open_website", "target": "google", "reply": "Opening Google."}
Command: "play kya baat hai" -> {"action": "play_music", "target": "kya baat hai", "reply": "Playing on YouTube."}
Command: "how are you" -> {"action": "chat", "target": null, "reply": "I am operating at full capacity, sir."}
"""

    # --- Build the request payload for the local Ollama-compatible server. ---
    payload = {
        "model": "phi3-local:latest",
        "prompt": f"{system_prompt}\n\nCommand: \"{command}\"\nJSON:",
        "stream": False,
        "format": "json"
    }

    try:
        # --- Send the command to the local AI server and wait for the response. ---
        response = requests.post("http://localhost:11434/api/generate", json=payload, timeout=10)
        response_data = response.json()

        # --- Extract the generated text from different response formats. ---
        if "response" in response_data:
            text_output = response_data["response"]
        elif "content" in response_data:
            text_output = response_data["content"]
        elif "text" in response_data:
            text_output = response_data["text"]
        else:
            text_output = str(response_data)

        # --- Convert the AI's text output into a real dictionary. ---
        return extract_and_parse(text_output)

    except requests.exceptions.ConnectionError:
        # --- If the local AI server is offline, tell the user politely and continue safely. ---
        print("[Error]: Could not connect to local AI server.")
        return {"action": "chat", "target": None, "reply": "Local server is offline."}
    except Exception as e:
        # --- Catch parsing or generation failures and return a safe fallback response. ---
        print(f"[Parser Error]: {e}")
        return {"action": "chat", "target": None, "reply": "I encountered an issue processing that request."}
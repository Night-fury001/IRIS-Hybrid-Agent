# --- This file contains the actual actions that IRIS performs, such as opening websites, playing music, and launching tools. ---
import webbrowser
import urllib.parse
import subprocess
import urllib.request
import re

# --- Open a website in the default browser using a clean URL. ---
def open_website(target):
    """Open a website in the default browser cleanly."""
    # --- Use a safe fallback if the user does not specify a site. ---
    if not target:
        target = "google"

    # --- Remove spaces so names like "google maps" are normalized. ---
    target_clean = target.lower().strip().replace(" ", "")

    # --- If the user already passed a full URL, keep it as-is. ---
    if target_clean.startswith("http://") or target_clean.startswith("https://"):
        url = target_clean
    elif "." in target_clean:
        # --- If the name already looks like a domain, add the protocol. ---
        url = f"https://{target_clean}"
    else:
        # --- Otherwise, assume the user wants a standard website in the .com domain. ---
        url = f"https://www.{target_clean}.com"

    # --- Launch the site in the system browser. ---
    webbrowser.open(url)

# --- Search YouTube and open the first matching video or fallback to a normal search page. ---
def play_music(target):
    """Directly launch and play the first matching YouTube video."""
    # --- If no song is given, open YouTube directly. ---
    if not target:
        webbrowser.open("https://www.youtube.com")
        return

    try:
        # --- Build a YouTube search URL and inspect the page for video IDs. ---
        search_query = urllib.parse.quote(target)
        search_url = f"https://www.youtube.com/results?search_query={search_query}"

        req = urllib.request.Request(
            search_url,
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        )
        html = urllib.request.urlopen(req).read().decode('utf-8')
        video_ids = re.findall(r"watch\?v=(\S{11})", html)

        # --- Open the first video found if a result is available. ---
        if video_ids:
            play_url = f"https://www.youtube.com/watch?v={video_ids[0]}"
            webbrowser.open(play_url)
            return
    except Exception as e:
        # --- If the direct search fails, print an error and fall back to the general search page. ---
        print(f"[Music Direct Play Error]: {e}, falling back to search query...")

    # --- Fallback to a normal YouTube search result page. ---
    fallback_query = urllib.parse.quote_plus(target)
    webbrowser.open(f"https://www.youtube.com/results?search_query={fallback_query}")

# --- Launch Visual Studio Code if it is installed and available in the system PATH. ---
def launch_vscode():
    """Launch Visual Studio Code."""
    try:
        # --- Use the system command to open the VS Code launcher. ---
        subprocess.Popen(["code"], shell=True)
    except Exception as e:
        # --- Show the error but do not stop the program. ---
        print(f"[Action Error]: Could not open VS Code: {e}")

# --- Start a new command window and show live NVIDIA GPU information. ---
def check_hardware():
    """Launch a separate terminal showing live GPU statistics without blocking Iris."""
    try:
        # --- This opens a separate Windows console window so the system stats stay visible. ---
        subprocess.Popen("start cmd /k nvidia-smi", shell=True)
    except Exception as e:
        # --- If GPU info cannot be shown, print the issue. ---
        print(f"[Action Error]: Could not query GPU stats: {e}")

# --- Helper function for routing a full intent dictionary into an action. ---
def execute_action(intent_data):
    """Router helper if called with full intent dictionary."""
    # --- Read the action and target values from the AI output. ---
    action = intent_data.get("action")
    target = intent_data.get("target")

    if action == "open_website":
        open_website(target)
    elif action == "play_music":
        play_music(target)
    elif action == "launch_vscode":
        launch_vscode()
    elif action == "check_hardware":
        check_hardware()
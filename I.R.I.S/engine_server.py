# --- This file checks whether the local AI server is running and starts it automatically when needed. ---
import socket
import subprocess
import time

# --- Local AI server manager ---
# This module checks whether the AI backend is running and starts it automatically if needed.

# --- Check if the local AI server is active on port 11434. ---
def is_local_ai_running():
    """Check if the local AI server is already active on port 11434."""

    # --- Try to connect to the local machine on port 11434. If it connects, the server is running. ---
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', 11434)) == 0

# --- Start the portable local AI server in the background when the port is closed. ---
def start_local_ai_background():
    """Automatically execute the portable chat script in the background if port 11434 is closed."""
    
    # --- Only start the server if it is not already running. ---
    if not is_local_ai_running():
        print("[System]: Local AI server is offline. Booting up portable environment...")
        try:
            # --- Path to the portable AI startup script. Update this path if your local model folder is stored somewhere else. ---
            bat_path = r"D:\USB-Uncensored-LLM-main\Windows\start-fast-chat.bat"

            # --- Start the portable environment in the background without opening a console window. ---
            subprocess.Popen(
                [bat_path],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                creationflags=subprocess.CREATE_NO_WINDOW,
                shell=True
            )

            # --- Wait a few seconds to allow the AI server to finish starting up. ---
            time.sleep(4)
        except Exception as e:
            # --- Show an error if the startup script cannot be launched. ---
            print(f"[Error]: Failed to auto-start portable environment: {e}")
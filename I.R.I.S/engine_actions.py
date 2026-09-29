import webbrowser
import pywhatkit
from engine_voice import speak

def open_website(target):
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    
    site_name = target.lower().replace(" ", "")
    url = f"https://www.{site_name}.com"
    
    speak(f"Opening {target}")
    print(f"---> Opening {url} in Chrome")
    webbrowser.get('chrome').open(url)

def play_music(target):
    speak(f"Playing {target}")
    print(f"---> Playing {target} on YouTube")
    pywhatkit.playonyt(target)
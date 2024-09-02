import eel
import subprocess
import time
from back.command import *

def start():
    eel.init("front")
    eel.start("index.html", mode=None ,host="localhost", port=8000, block=False)

    time.sleep(2)

    chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"  # Adjust if needed
    url = "http://localhost:8000/index.html"

    subprocess.Popen([chrome_path, "--app=" + url])

    eel.sleep(1000)

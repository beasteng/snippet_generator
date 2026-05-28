"""04 — Daemon threads.
INTERVIEW TIP: Daemon threads are killed when the main thread exits.
Use daemon=True for background tasks you don't need to wait for.
Non-daemon threads keep the process alive until they finish.
"""
import threading
import time

def background():
    while True:
        print("background tick")
        time.sleep(0.5)

t = threading.Thread(target=background, daemon=True)
t.start()
time.sleep(1.5)
print("Main exiting — daemon thread will be killed")

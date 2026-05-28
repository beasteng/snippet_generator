"""02 — Passing arguments to threads.
INTERVIEW TIP: Use args=(...,) tuple for positional args,
kwargs={} for keyword args.
"""
import threading

def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

t = threading.Thread(target=greet, args=("Alice",), kwargs={"greeting": "Hi"})
t.start()
t.join()

"""16 — Pipe for two-way communication.
INTERVIEW TIP: Pipe() returns two Connection objects.
Faster than Queue for simple 1-to-1 communication.
"""
from multiprocessing import Process, Pipe

def child(conn):
    conn.send({"msg": "hello from child", "pid": __import__("os").getpid()})
    conn.close()

if __name__ == "__main__":
    parent_conn, child_conn = Pipe()
    p = Process(target=child, args=(child_conn,))
    p.start()
    print(parent_conn.recv())
    p.join()

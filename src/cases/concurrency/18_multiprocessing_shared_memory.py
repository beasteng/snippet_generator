"""18 — SharedMemory (Python 3.8+).
INTERVIEW TIP: Zero-copy shared memory between processes.
Much faster than Manager for large data (e.g. NumPy arrays).
Remember to .close() and .unlink().
"""
from multiprocessing import Process
from multiprocessing.shared_memory import SharedMemory

def child(name):
    shm = SharedMemory(name=name)
    shm.buf[:5] = b"hello"
    shm.close()

if __name__ == "__main__":
    shm = SharedMemory(create=True, size=10)
    p = Process(target=child, args=(shm.name,))
    p.start()
    p.join()
    print(bytes(shm.buf[:5]))  # b'hello'
    shm.close()
    shm.unlink()

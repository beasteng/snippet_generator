"""19 — Manager for shared complex objects.
INTERVIEW TIP: Manager creates a server process that holds
the real objects; proxies handle synchronisation.
Slower than Value/Array but supports dict, list, Namespace, etc.
"""
from multiprocessing import Process, Manager

def append_item(shared_list, item):
    shared_list.append(item)

if __name__ == "__main__":
    with Manager() as mgr:
        lst = mgr.list()
        ps = [Process(target=append_item, args=(lst, i)) for i in range(5)]
        for p in ps:
            p.start()
        for p in ps:
            p.join()
        print(sorted(lst))  # [0, 1, 2, 3, 4]

"""
21 — Parallel Tool Execution
===============================
Run independent tools concurrently.
Interview point: Parallel execution reduces latency when tools
  don't depend on each other.
"""
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

def search_web(query: str) -> str:
    time.sleep(0.3)  # Simulate network latency
    return f"Web: results for '{query}'"

def search_database(query: str) -> str:
    time.sleep(0.2)
    return f"DB: records matching '{query}'"

def search_cache(query: str) -> str:
    time.sleep(0.05)
    return f"Cache: hit for '{query}'"

def parallel_search(query: str) -> dict[str, str]:
    tools = {
        "web": search_web,
        "database": search_database,
        "cache": search_cache,
    }
    results = {}
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = {
            executor.submit(fn, query): name
            for name, fn in tools.items()
        }
        for future in as_completed(futures):
            name = futures[future]
            results[name] = future.result()
            print(f"  ✓ {name} completed")
    return results

if __name__ == "__main__":
    start = time.time()
    results = parallel_search("AI agents")
    elapsed = time.time() - start
    print(f"\nAll results ({elapsed:.2f}s):")
    for name, result in results.items():
        print(f"  {name}: {result}")

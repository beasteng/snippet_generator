# 🐍 Asyncio Masterclass — 30 Interview-Ready Snippets

## Structure

| Part | Files | Level |
|------|-------|-------|
| 1. Fundamentals | 01–06 | 🟢 Basic |
| 2. Intermediate Patterns | 07–14 | 🟡 Intermediate |
| 3. Synchronization Primitives | 15–18 | 🟠 Advanced |
| 4. Advanced Flow Control | 19–23 | 🔴 Advanced+ |
| 5. Networking | 24–25 | 🔴 Advanced+ |
| 6. Expert-Level | 26–30 | ⚫ Expert |

## Run any file

```bash
python 01_hello_async.py
```

## Requirements

- Python 3.9+ (3.11+ for TaskGroup and Barrier)
- `pip install aiohttp` (only for file 10)

## TCP Echo Demo (files 24 + 25)

```bash
# Terminal 1
python 24_stream_tcp_server.py

# Terminal 2
python 25_stream_tcp_client.py
```

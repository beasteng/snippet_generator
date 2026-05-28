# 🌶️ Flask Masterclass — 30 Interview-Ready Snippets

## Quick Start

```bash
pip install -r requirements.txt
python 01_hello_world.py
# Open http://127.0.0.1:5001
```

## Structure

| Part | Files | Level | Topics |
|------|-------|-------|--------|
| 1. Fundamentals | 01–06 | 🟢 Basic | Routes, methods, JSON, query params, templates |
| 2. Intermediate | 07–14 | 🟡 Intermediate | Blueprints, factory, errors, middleware, sessions, uploads, logging |
| 3. Auth & Security | 15–18 | 🟠 Advanced | Basic auth, token auth, password hashing, CORS |
| 4. Database | 19–22 | 🔴 Advanced+ | SQLite CRUD, SQLAlchemy ORM, migrations, repository pattern |
| 5. Advanced Patterns | 23–26 | 🔴 Advanced+ | Caching, rate limiting, SSE streaming, background tasks |
| 6. Production | 27–30 | ⚫ Expert | Testing, CLI commands, API versioning, production app |

## Ports

Each file runs on a unique port (5001–5030) so you can run multiple simultaneously.

## Run Tests (file 27)

```bash
python -m pytest 27_testing.py -v
```

## Run CLI Commands (file 28)

```bash
export FLASK_APP=28_cli_commands.py
flask seed --count 10
flask info
flask health-check
```

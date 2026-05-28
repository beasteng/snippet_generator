"""#23 — asyncio.create_subprocess_exec: run external processes asynchronously."""
import asyncio


async def run_command(cmd: list[str]) -> tuple[str, str, int]:
    proc = await asyncio.create_subprocess_exec(
        *cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await proc.communicate()
    return stdout.decode().strip(), stderr.decode().strip(), proc.returncode


async def main():
    commands = [
        ["python", "-c", "print('hello from subprocess')"],
        ["python", "-c", "import sys; sys.exit(1)"],
        ["python", "-c", "import platform; print(platform.python_version())"],
    ]

    for cmd in commands:
        out, err, code = await run_command(cmd)
        print(f"  cmd={' '.join(cmd[-1:])}  exit={code}  out='{out}'  err='{err}'")


if __name__ == "__main__":
    asyncio.run(main())

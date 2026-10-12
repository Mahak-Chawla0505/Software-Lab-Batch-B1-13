import subprocess


command = input("Enter command: ").strip()

# Safer alternative: only allow a limited list of commands and avoid shell=True.
allowed_commands = {
    "echo": ["echo"],
    "date": ["date"],
    "whoami": ["whoami"],
}

if command in allowed_commands:
    subprocess.run(allowed_commands[command], check=True)
else:
    print("Unsupported command.")

# utils.py

import json
from pathlib import Path

HISTORY_FILE = Path("data/history.json")

def save_to_history(entry):
    # Load existing history
    if HISTORY_FILE.exists():
        with open(HISTORY_FILE, "r") as file:
            history = json.load(file)
    else:
        history = []

    # Add new entry
    history.append(entry)

    # Save back
    with open(HISTORY_FILE, "w") as file:
        json.dump(history, file, indent=4)

def get_history():
    if HISTORY_FILE.exists():
        with open(HISTORY_FILE, "r") as file:
            return json.load(file)
    return []
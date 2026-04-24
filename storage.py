import json
import os

DATA_PATH = "data/tasks.json"


def load_tasks():
    if not os.path.exists("data"):
        os.makedirs("data")

    if not os.path.exists(DATA_PATH):
        return []

    try:
        with open(DATA_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []


def save_tasks(tasks):
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=4)
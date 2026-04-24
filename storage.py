import json

FILE = "data/tasks.json"

def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f)

def load_tasks():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []
import os

FILE_PATH = "data/tasks.txt"

def initialize_storage():
    if not os.path.exists("data"):
        os.makedirs("data")

    if not os.path.exists(FILE_PATH):
        open(FILE_PATH, "w").close()

def load_tasks():
    initialize_storage()
    with open(FILE_PATH, "r") as f:
        return [line.strip() for line in f if line.strip()]

def save_tasks(tasks):
    with open(FILE_PATH, "w") as f:
        for task in tasks:
            f.write(task + "\n")
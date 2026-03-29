import os

FILE_PATH = "data/tasks.txt"

# Create folder/file if not exists
if not os.path.exists("data"):
    os.makedirs("data")

if not os.path.exists(FILE_PATH):
    open(FILE_PATH, "w").close()

def load_tasks():
    tasks = []
    with open(FILE_PATH, "r") as f:
        for line in f:
            task = line.strip()
            if task:
                tasks.append(task)
    return tasks

def save_tasks(tasks):
    with open(FILE_PATH, "w") as f:
        for task in tasks:
            f.write(task + "\n")

            
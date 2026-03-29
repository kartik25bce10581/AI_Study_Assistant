import tkinter as tk
from tkinter import messagebox
import os

FILE_PATH = "data/tasks.txt"

# Auto-create data folder & file
if not os.path.exists("data"):
    os.makedirs("data")

if not os.path.exists(FILE_PATH):
    open(FILE_PATH, "w").close()

tasks = []

# COLORS
BG = "#121212"
CARD = "#1e1e1e"
TEXT = "#ffffff"
ACCENT = "#4CAF50"
BUTTON = "#2c2c2c"

# ---------------- CHATBOT ----------------
def chatbot_response(q):
    q = q.lower()

    if "revise" in q:
        return "Use active recall + spaced repetition."
    elif "focus" in q:
        return "Study in distraction-free environment."
    elif "exam" in q:
        return "Practice PYQs + time management."
    elif "motivation" in q:
        return "Discipline > Motivation. Start small."
    elif "memory" in q:
        return "Use mnemonics + repeated revision."
    elif "practice" in q:
        return "Solve problems daily and analyze mistakes."
    elif "plan" in q:
        return "Make a realistic daily timetable."
    elif "stress" in q:
        return "Take breaks + deep breathing."
    elif "sleep" in q:
        return "7-8 hours sleep improves learning."
    elif "notes" in q:
        return "Keep notes short, clear, and visual."
    elif "backlog" in q:
        return "Divide backlog into small chunks and start."
    elif "consistency" in q:
        return "Small daily progress beats irregular effort."
    else:
        return "Ask about study, revision, focus, exams, etc."

# ---------------- FILE ----------------
def save_tasks():
    with open(FILE_PATH, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def load_tasks():
    with open(FILE_PATH, "r") as f:
        for line in f:
            task = line.strip()
            if task:
                tasks.append(task)
                task_list.insert(tk.END, "• " + task)

# ---------------- TASK ----------------
def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        task_list.insert(tk.END, "• " + task)
        task_entry.delete(0, tk.END)
        save_tasks()
        update_stats()
    else:
        messagebox.showwarning("Warning", "Enter a task!")

def delete_task():
    try:
        selected = task_list.curselection()[0]
        task_list.delete(selected)
        tasks.pop(selected)
        save_tasks()
        update_stats()
    except:
        messagebox.showwarning("Warning", "Select a task!")

def clear_tasks():
    tasks.clear()
    task_list.delete(0, tk.END)
    save_tasks()
    update_stats()

# ---------------- ANALYTICS ----------------
def update_stats():
    total = len(tasks)
    stats_label.config(text=f"📊 Total Tasks: {total}")

# ---------------- CHAT ----------------
def ask_ai():
    q = question_entry.get()
    if q:
        ans = chatbot_response(q)
        answer_label.config(text="💡 " + ans)
        question_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Enter a question!")

# ---------------- UI ----------------
root = tk.Tk()
root.title("AI Study Assistant")
root.geometry("650x650")
root.configure(bg=BG)

tk.Label(root, text="📚 AI Study Assistant",
         font=("Arial", 18, "bold"),
         bg=BG, fg=ACCENT).pack(pady=10)

# TASK FRAME
task_frame = tk.Frame(root, bg=CARD, padx=10, pady=10)
task_frame.pack(padx=15, pady=10, fill="x")

tk.Label(task_frame, text="📝 Study Tasks",
         bg=CARD, fg=TEXT).pack(anchor="w")

task_entry = tk.Entry(task_frame, bg=BG, fg=TEXT)
task_entry.pack(fill="x", pady=5)

btn_frame = tk.Frame(task_frame, bg=CARD)
btn_frame.pack()

tk.Button(btn_frame, text="Add", command=add_task,
          bg=BUTTON, fg=TEXT).pack(side="left", padx=5)

tk.Button(btn_frame, text="Delete", command=delete_task,
          bg="#aa0000", fg=TEXT).pack(side="left", padx=5)

tk.Button(btn_frame, text="Clear All", command=clear_tasks,
          bg="#8B0000", fg=TEXT).pack(side="left", padx=5)

task_list = tk.Listbox(task_frame, bg=BG, fg=TEXT, height=6)
task_list.pack(fill="x", pady=10)

# STATS
stats_label = tk.Label(task_frame, text="📊 Total Tasks: 0",
                       bg=CARD, fg=ACCENT)
stats_label.pack()

# AI FRAME
ai_frame = tk.Frame(root, bg=CARD, padx=10, pady=10)
ai_frame.pack(padx=15, pady=10, fill="x")

tk.Label(ai_frame, text="🤖 AI Assistant",
         bg=CARD, fg=TEXT).pack(anchor="w")

question_entry = tk.Entry(ai_frame, bg=BG, fg=TEXT)
question_entry.pack(fill="x", pady=5)

tk.Button(ai_frame, text="Ask AI", command=ask_ai,
          bg=BUTTON, fg=TEXT).pack(pady=5)

answer_label = tk.Label(ai_frame,
                        text="💡 Ask me anything about studying!",
                        wraplength=500,
                        bg=CARD, fg=TEXT)
answer_label.pack(pady=10)

# LOAD DATA
load_tasks()
update_stats()

root.mainloop()



  
import tkinter as tk
from tkinter import messagebox
from chatbot import chatbot_response
from task_manager import load_tasks, save_tasks

BG = "#121212"
CARD = "#1e1e1e"
TEXT = "#ffffff"
ACCENT = "#4CAF50"
BUTTON = "#2c2c2c"

class App:
    def __init__(self, root):
        self.root = root
        self.tasks = load_tasks()

        self.setup_ui()
        self.load_tasks_to_ui()

    def setup_ui(self):
        self.root.title("AI Study Assistant")
        self.root.geometry("650x650")
        self.root.configure(bg=BG)

        tk.Label(self.root, text="📚 AI Study Assistant",
                 font=("Arial", 18, "bold"),
                 bg=BG, fg=ACCENT).pack(pady=10)

        # Task Frame
        frame = tk.Frame(self.root, bg=CARD, padx=10, pady=10)
        frame.pack(padx=15, pady=10, fill="x")

        tk.Label(frame, text="📝 Study Tasks", bg=CARD, fg=TEXT).pack(anchor="w")

        self.task_entry = tk.Entry(frame, bg=BG, fg=TEXT)
        self.task_entry.pack(fill="x", pady=5)

        btn_frame = tk.Frame(frame, bg=CARD)
        btn_frame.pack()

        tk.Button(btn_frame, text="Add", command=self.add_task,
                  bg=BUTTON, fg=TEXT).pack(side="left", padx=5)

        tk.Button(btn_frame, text="Delete", command=self.delete_task,
                  bg="#aa0000", fg=TEXT).pack(side="left", padx=5)

        tk.Button(btn_frame, text="Clear All", command=self.clear_tasks,
                  bg="#8B0000", fg=TEXT).pack(side="left", padx=5)

        self.task_list = tk.Listbox(frame, bg=BG, fg=TEXT, height=6)
        self.task_list.pack(fill="x", pady=10)

        self.stats = tk.Label(frame, text="", bg=CARD, fg=ACCENT)
        self.stats.pack()

        # AI Frame
        ai = tk.Frame(self.root, bg=CARD, padx=10, pady=10)
        ai.pack(padx=15, pady=10, fill="x")

        tk.Label(ai, text="🤖 AI Assistant", bg=CARD, fg=TEXT).pack(anchor="w")

        self.question = tk.Entry(ai, bg=BG, fg=TEXT)
        self.question.pack(fill="x", pady=5)

        tk.Button(ai, text="Ask AI", command=self.ask_ai,
                  bg=BUTTON, fg=TEXT).pack(pady=5)

        self.answer = tk.Label(ai, text="💡 Ask me anything!",
                               wraplength=500,
                               bg=CARD, fg=TEXT)
        self.answer.pack(pady=10)

    def load_tasks_to_ui(self):
        for task in self.tasks:
            self.task_list.insert(tk.END, "• " + task)
        self.update_stats()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_list.insert(tk.END, "• " + task)
            self.task_entry.delete(0, tk.END)
            save_tasks(self.tasks)
            self.update_stats()
        else:
            messagebox.showwarning("Warning", "Enter a task!")

    def delete_task(self):
        try:
            index = self.task_list.curselection()[0]
            self.task_list.delete(index)
            self.tasks.pop(index)
            save_tasks(self.tasks)
            self.update_stats()
        except:
            messagebox.showwarning("Warning", "Select a task!")

    def clear_tasks(self):
        self.tasks.clear()
        self.task_list.delete(0, tk.END)
        save_tasks(self.tasks)
        self.update_stats()

    def update_stats(self):
        self.stats.config(text=f"📊 Total Tasks: {len(self.tasks)}")

    def ask_ai(self):
        q = self.question.get()
        if q:
            ans = chatbot_response(q)
            self.answer.config(text="💡 " + ans)
            self.question.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Enter a question!")

            
import tkinter as tk
from logic import TaskManager


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-do List App")

        self.manager = TaskManager()

        # UI
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=5)

        tk.Button(root, text="Add", command=self.add_task).pack()
        tk.Button(root, text="Delete", command=self.delete_task).pack()
        tk.Button(root, text="Clear", command=self.clear_tasks).pack()

        self.listbox = tk.Listbox(root, width=50)
        self.listbox.pack(pady=10)

        self.load_tasks_to_ui()

    def load_tasks_to_ui(self):
        for task in self.manager.get_tasks():
            self.listbox.insert("end", task)

    def add_task(self):
        task = self.entry.get().strip()
        if task:
            self.manager.add_task(task)
            self.listbox.insert("end", task)
            self.entry.delete(0, "end")

    def delete_task(self):
        selected = self.listbox.curselection()
        if selected:
            task = self.listbox.get(selected)
            self.manager.delete_task(task)
            self.listbox.delete(selected)

    def clear_tasks(self):
        self.manager.clear_tasks()
        self.listbox.delete(0, "end")
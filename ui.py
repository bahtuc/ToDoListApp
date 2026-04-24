import tkinter as tk
from logic import add_task, delete_task

def start_app():
    root = tk.Tk()
    root.title("To-DO App")
    root.geometry("400x500")

    global entry, listbox

    entry= tk.Entry(root)
    entry.pack()
    btn_add= tk.Button(root, text="Add", command=lambda: add_task(entry,listbox))
    btn_add.pack()

    btn_delete = tk.Button(root, text="Delete", command=lambda: delete_task(listbox))
    btn_delete.pack()
    listbox = tk.Listbox(root)
    listbox.pack()

    root.mainloop()
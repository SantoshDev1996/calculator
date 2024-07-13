import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        self.tasks = []

        # Create GUI elements
        self.task_entry = tk.Entry(self.root, width=80)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        add_task_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        add_task_button.grid(row=0, column=1, padx=10, pady=10)

        self.task_listbox = tk.Listbox(self.root, width=80, height=30)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        remove_task_button = tk.Button(self.root, text="Remove Task", command=self.remove_task)
        remove_task_button.grid(row=2, column=0, padx=10, pady=10)

        clear_tasks_button = tk.Button(self.root, text="Clear All", command=self.clear_tasks)
        clear_tasks_button.grid(row=2, column=1, padx=10, pady=10)

        # Populate listbox with existing tasks
        self.refresh_task_listbox()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.refresh_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def remove_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_index]
            self.refresh_task_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to remove.")

    def clear_tasks(self):
        self.tasks = []
        self.refresh_task_listbox()

    def refresh_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()

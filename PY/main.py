import os
import json
from datetime import datetime

# File to store tasks
TASK_FILE = "tasks.json"

# Function to load tasks from the JSON file
def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            return json.load(file)
    return []

# Function to save tasks to the JSON file
def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Function to add a new task
def add_task():
    task = input("Enter the task: ")
    priority = input("Set priority (High/Medium/Low): ").capitalize()
    due_date = input("Enter due date (YYYY-MM-DD) or leave blank: ")

    task_data = {
        "task": task,
        "priority": priority if priority in ["High", "Medium", "Low"] else "Medium",
        "due_date": due_date if due_date else None,
        "completed": False
    }

    tasks = load_tasks()
    tasks.append(task_data)
    save_tasks(tasks)
    print("✅ Task added successfully!")

# Function to display tasks
def view_tasks(show_completed=False):
    tasks = load_tasks()
    if not tasks:
        print("No tasks found!")
        return

    for idx, task in enumerate(tasks, start=1):
        if show_completed or not task["completed"]:
            status = "✅ Completed" if task["completed"] else "⏳ Pending"
            due = f" (Due: {task['due_date']})" if task['due_date'] else ""
            print(f"{idx}. {task['task']} [{task['priority']}] - {status}{due}")

# Function to mark a task as completed
def mark_task_completed():
    tasks = load_tasks()
    view_tasks()

    try:
        task_num = int(input("Enter the task number to mark as completed: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks[task_num]["completed"] = True
            save_tasks(tasks)
            print("🎉 Task marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Function to delete a task
def delete_task():
    tasks = load_tasks()
    view_tasks()

    try:
        task_num = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_num < len(tasks):
            deleted_task = tasks.pop(task_num)
            save_tasks(tasks)
            print(f"🗑️ Task '{deleted_task['task']}' deleted!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main menu for user interaction
def main():
    while True:
        print("\n--- AutoTasker Menu ---")
        print("1️⃣  Add Task")
        print("2️⃣  View Pending Tasks")
        print("3️⃣  View All Tasks")
        print("4️⃣  Mark Task as Completed")
        print("5️⃣  Delete Task")
        print("6️⃣  Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks(show_completed=False)
        elif choice == "3":
            view_tasks(show_completed=True)
        elif choice == "4":
            mark_task_completed()
        elif choice == "5":
            delete_task()
        elif choice == "6":
            print("👋 Goodbye!")
            break
        else:
            print("❗ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
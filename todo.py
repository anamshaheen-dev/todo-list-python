# To-Do List App
# Built by: Anum Shaheen

import os

FILENAME = "tasks.txt"

def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return [line.strip() for line in f.readlines()]
    return []

def save_tasks():
    with open(FILENAME, "w") as f:
        for task in tasks:
            f.write(task + "\n")

tasks = load_tasks()

def add_task(task):
    tasks.append(task)
    save_tasks()
    print(f'Task "{task}" added successfully!')

def view_tasks():
    if len(tasks) == 0:
        print("Your to-do list is empty!")
    else:
        print("\n--- Your Tasks ---")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        print("------------------")

def delete_task(task_number):
    if task_number < 1 or task_number > len(tasks):
        print("Invalid task number!")
    else:
        removed = tasks.pop(task_number - 1)
        save_tasks()
        print(f'Task "{removed}" deleted!')

def menu():
    print("\n==========================")
    print("      To-Do List App      ")
    print("==========================")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    while True:
        choice = input("\nEnter choice (1/2/3/4): ")

        if choice == '1':
            task = input("Enter task: ")
            add_task(task)

        elif choice == '2':
            view_tasks()

        elif choice == '3':
            view_tasks()
            task_num = int(input("Enter task number to delete: "))
            delete_task(task_num)

        elif choice == '4':
            print("Goodbye! Stay productive!")
            break

        else:
            print("Invalid choice! Please enter 1, 2, 3 or 4.")

# This runs the app
menu()
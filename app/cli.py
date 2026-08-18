from storage import save_tasks, return_tasks 
from manager import TaskManager
from models import Task
from datetime import datetime

task_manager = TaskManager()

def display_menu():
    print("=== Gestionnaire de tâches ===")
    print("1. Add a new task")
    print("2. Display all tasks")
    print("3. Display tasks by priority")
    print("4. Display tasks by done status")
    print("5. Mark a task as done")
    print("6. Modify a task")
    print("7. Delete a task")
    print("8. Quit")

def start_app():
    while True:
        display_menu()
        choice = input("Choose an option (1-8): ")
        if choice == '1':
            task = Task(
                id=None,
                title=input("Enter task title: "),
                creation_date=datetime.today(),
                priority=input("Enter task priority: ")
            )
            task_manager.add_task(task)
        elif choice == '2':
            task_manager.display_tasks()
        elif choice == '3':
            priority = input("Enter the priority to filter by (low / medium / high): ")
            if priority.lower() not in ["low", "medium", "high"]:
                print("Invalid priority. Please try again.")
                continue
            filtered_tasks = task_manager.filter_tasks_by_priority(priority)
            for task in filtered_tasks:
                print(f"ID: {task.id}, Title: {task.title}, Priority: {task.priority}, Done: {task.done}")
        elif choice == '4':
            done_status = input("Enter the done status to filter by (done / not started / in progress): ")
            if done_status.lower() == "done":
                done_status = "done"
            elif done_status.lower() == "not started":
                done_status = "not started"
            elif done_status.lower() == "in progress":
                done_status = "in progress"
            else:
                print("Invalid option. Please try again.")
        elif choice == '5':
            task_title = input("Enter the title of the task to mark as done: ")
            if task_manager.finish_task(task_title):
                print(f"Task '{task_title}' marked as done.")
            else:
                print(f"Task '{task_title}' not found.")
        elif choice == '6':
            task_title = input("Enter the title of the task to modify: ")
            new_title = input("Enter the new title for the task: ")
            if task_manager.modify_task(task_title, new_title):
                print(f"Task '{task_title}' modified successfully.")
            else:
                print(f"Task '{task_title}' not found.")
        elif choice == '7':
            task_title = input("Enter the title of the task to delete: ")
            task = task_manager.get_task_by_title(task_title)
            if task:
                task_manager.remove_task(task)
                print(f"Task '{task_title}' deleted successfully.")
            else:
                print(f"Task '{task_title}' not found.")
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
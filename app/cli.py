from storage import save_tasks, return_tasks 
from manager import TaskManager
from models import TaskPriority
from models import TaskStatus

DATA_FILE = "../data/backup.json"

def display_menu():
    print("=== Gestionnaire de tâches ===")
    print("1. Add a new task")
    print("2. Display all tasks")
    print("3. Display tasks by priority")
    print("4. Display tasks by status")
    print("5. Mark a task as done")
    print("6. Modify task's priority")
    print("7. Modify task's status")
    print("8. Delete a task")
    print("9. Quit")

def start_app():
    task_manager = TaskManager(return_tasks(DATA_FILE))
    while True:
        display_menu()
        choice = input("Choose an option (1-9): ")
        if choice == '1':
            title=input("Enter task title (required): ")
            priority=input("Enter task priority (3.low / 2.medium / 1.high): ")
            try:
                priority = TaskPriority._priority_transform(priority).value
            except ValueError:
                print("Invalid priority choice. Please try again.")
                continue
            description=input("Enter task description (optional): ")        
            task_manager.add_task(title, priority, description)
        elif choice == '2':
            task_manager.display_tasks()
        elif choice == '3':
            priority = input("Enter the priority to filter by (3.low / 2.medium / 1.high): ")
            try:
                priority = TaskPriority._priority_transform(priority).value
            except ValueError:
                print("Invalid priority choice. Please try again.")
                continue
            if task_manager.filter_tasks_by_priority(priority):
                print(f"Tasks with priority '{priority}':")
                filtered_tasks = task_manager.filter_tasks_by_priority(priority)
                for task in filtered_tasks:
                    print(f"ID: {task.id}, Title: {task.title}, Priority: {task.priority}, Status: {task.status}")
                    print("----")
            else:
                print(f"No tasks found with priority '{priority}' in the backup.")
        elif choice == '4':
            status = input("Enter the done status to filter by (3.done / 2.not started / 1.in progress): ")

            try: 
                status = TaskStatus._status_transform(status).value
            except ValueError:
                print("Invalid done status choice. Please try again.")
                continue
            if task_manager.filter_tasks_by_done_status(status):
                print(f"Tasks with done status '{status}':")
                filtered_tasks = task_manager.filter_tasks_by_done_status(status)
                for task in filtered_tasks:
                    print(f"ID: {task.id}, Title: {task.title}, Priority: {task.priority}, Status: {task.status}")
                    print("----")
            else:
                print(f"No tasks found with done status '{status}'in the backup.")
        elif choice == '5':
            task_id = input("Enter the id of the task to mark as done: ")
            try: 
                task_id = int(task_id)
            except ValueError:
                print("Invalid task ID. Please enter a valid integer.")
                continue
            if task_manager.get_task_by_id(task_id):
                task_manager.finish_task(task_id)
                print(f"Task '{task_id}' marked as done.")
            else:
                print(f"Task '{task_id}' not found.")
                continue
        elif choice == '6':
            task_id = input("Enter the id of the task to modify its priority: ")
            try: 
                task_id = int(task_id)
            except ValueError:  
                print("Invalid task ID. Please enter a valid integer.")
                continue
            if task_manager.get_task_by_id(task_id):
                new_priority = input("Enter the new priority for the task (3.low / 2.medium / 1.high): ")
                try: 
                    new_priority = TaskPriority._priority_transform(new_priority).value
                    task_manager.change_task_priority(task_id, new_priority)
                    print(f"Task '{task_id}' priority changed to '{new_priority}'.")
                except ValueError:
                    print("Invalid priority choice. Please try again.")
        elif choice == '7':
            task_id = input("Enter the id of the task to modify its status: ")
            try: 
                task_id = int(task_id)
            except ValueError:
                print("Invalid task ID. Please enter a valid integer.")
                continue
            if task_manager.get_task_by_id(task_id):
                new_status = input("Enter the new status for the task (3.done / 2.not started / 1.in progress): ")
                try:
                    new_status = TaskStatus._status_transform(new_status).value
                    task_manager.change_task_status(task_id, new_status)
                    print(f"Task '{task_id}' status changed to '{new_status}'.")
                    continue
                except ValueError:
                    print("Invalid status choice. Please try again.")
        elif choice == '8':
            task_id = input("Enter the id of the task to delete: ")
            try: 
                task_id = int(task_id)
            except ValueError:
                print("Invalid task ID. Please enter a valid integer.")
                continue
            if task_manager.get_task_by_id(task_id):
                task_manager.remove_task(task_id)
                print(f"Task '{task_id}' deleted.")
            else:
                print(f"Task with id '{task_id}' not found.")
                continue
        elif choice == '9':
            print("Exiting the application.")
            save_tasks(task_manager.get_tasks(), DATA_FILE)
            break
        else:
            print("Invalid option. Please try again.")
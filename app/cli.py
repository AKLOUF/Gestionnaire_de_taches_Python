from storage import save_tasks, return_tasks 
from manager import TaskManager
from models import TaskPriority
from models import TaskStatus

task_manager = TaskManager()

def display_menu():
    print("=== Gestionnaire de tâches ===")
    print("1. Add a new task")
    print("2. Display all tasks")
    print("3. Display tasks by priority")
    print("4. Display tasks by done status")
    print("5. Mark a task as done")
    print("6. Modify task's priority")
    print("7. Modify task's status")
    print("8. Delete a task")
    print("9. Quit")

def start_app():
    while True:
        display_menu()
        choice = input("Choose an option (1-9): ")
        if choice == '1':
            title=input("Enter task title (required): ")
            priority=input("Enter task priority (3.low / 2.medium / 1.high): ")
            if TaskPriority.__priority_from_choice(priority):
                priority = TaskPriority.__priority_from_choice(priority).value
            else:
                print("Invalid priority choice. Please try again.")
                continue
            description=input("Enter task description (optional): ")        
            task_manager.add_task(title, priority, description)
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
            done_status = input("Enter the done status to filter by (3.done / 2.not started / 1.in progress): ")

            if TaskStatus.__status_from_choice(done_status):
                done_status = TaskStatus.__status_from_choice(done_status).value
                if task_manager.filter_tasks_by_done_status(done_status):
                    print(f"Tasks with done status '{done_status}':")
                    for task in task_manager.filter_tasks_by_done_status(done_status):
                        print(f"ID: {task.id}, Title: {task.title}, Priority: {task.priority}, Done: {task.done}")
                        print("----")
                else:
                    print(f"No tasks found with done status '{done_status}'in the backup.")
        elif choice == '5':
            task_id = input("Enter the id of the task to mark as done: ")
            if task_manager.get_task_by_id(task_id):
                task_manager.finish_task(task_id)
                print(f"Task '{task_id}' marked as done.")
            else:
                raise ValueError(f"Task '{task_id}' not found.")
        elif choice == '6':
            task_id = input("Enter the id of the task to modify its priority: ")
            if task_manager.get_task_by_id(task_id):
                new_priority = input("Enter the new priority for the task (3.low / 2.medium / 3.high): ")
                if TaskPriority.__priority_from_choice(new_priority):
                    new_priority = TaskPriority.__priority_from_choice(new_priority).value
                    task_manager.change_task_priority(task_id, new_priority)
                    print(f"Task '{task_id}' priority changed to '{new_priority}'.")
                    continue
                else:
                    raise ValueError(f"Task with id '{task_id}' not found.")
        elif choice == '7':
            task_id = input("Enter the id of the task to modify its status: ")
            if task_manager.get_task_by_id(task_id):
                new_status = input("Enter the new status for the task (3.done / 2.not started / 3.in progress): ")
                if TaskStatus.__status_from_choice(new_status):
                    new_status = TaskStatus.__status_from_choice(new_status).value
                    task_manager.change_task_status(task_id, new_status)
                    print(f"Task '{task_id}' status changed to '{new_status}'.")
                    continue
            else:
                raise ValueError(f"Task with id '{task_id}' not found.")
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
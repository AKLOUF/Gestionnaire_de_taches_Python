import json
from app.models import Task 

def save_tasks(tasks, filename):
    try:
        with open(filename, 'w') as file:
            json.dump([task.to_dict() for task in tasks], file)
    except FileNotFoundError:
        print(f"File {filename} not found. Returning an empty task list.")
    except json.JSONDecodeError:
        print(f"Error decoding JSON from {filename}. Returning an empty task list.")
    except Exception as e:
        print(f"An error occurred while reading {filename}: {e}. Returning an empty task list.")
    return 0

def return_tasks(filename):
    tasks = []
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            for task_data in data:
                try:
                    task = Task.from_dict(task_data)
                    tasks.append(task)
                except Exception as e:
                    print(f"Error creating task from data {task_data}: {e}")
    except Exception as e:
        print(f"An error occurred while reading {filename}: {e}. Returning an empty task list.")
    return tasks
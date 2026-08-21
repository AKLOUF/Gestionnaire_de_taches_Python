import pytest
from storage import save_tasks, return_tasks
from manager import TaskManager
from models import Task, TaskStatus, TaskPriority
from datetime import datetime
import json

title = "Test Task"
priority = TaskPriority.HIGH.value
description = "This is a test task."

def test_save_tasks(tmp_path):
    data_file = tmp_path / "test_backup.json"
    task_manager = TaskManager()
    task_manager.add_task(title, priority, description)
    task_manager.add_task("Another Task", priority)

    save_tasks(task_manager.get_tasks(), str(data_file))

    with open(data_file, 'r') as file:
        saved_data = json.load(file)

    assert len(saved_data) == 2
    assert saved_data[0]['title'] == title
    assert saved_data[0]['priority'] == priority
    assert saved_data[0]['description'] == description
    assert saved_data[0]['status'] == TaskStatus.NOT_STARTED.value
    assert saved_data[1]['title'] == "Another Task"

def test_return_tasks(tmp_path):
    data_file = tmp_path / "test_backup.json"
    task_manager = TaskManager()
    task_manager.add_task(title, priority, description)
    save_tasks(task_manager.get_tasks(), str(data_file))

    return_task = return_tasks(data_file)
    assert return_task[0].id == 1
    assert return_task[0].title == title
    assert return_task[0].priority == priority
    assert return_task[0].description == description
    assert return_task[0].creation_date == datetime.today().strftime("%d-%m-%Y")
    assert return_task[0].status == TaskStatus.NOT_STARTED.value


def test_return_tasks_unexistant_file():
    task_manager = TaskManager()
    task_manager.add_task(title, priority, description)

    return_data = return_tasks("unexistant_file.json")
    
    assert return_data == []

def test_return_tasks_invalid_json(tmp_path):
    data_file = tmp_path / "corrupted.json"
    data_file.write_text("ceci n'est pas du JSON valide {{{")

    return_data = return_tasks(str(data_file))

    assert return_data == []

def test_save_tasks_empty_list(tmp_path):
    data_file = tmp_path / "test_backup.json"
    assert save_tasks([], str(data_file)) == True

def test_save_tasks_invalid_path():
    assert save_tasks([], "unexistant_folder/backup.json") == False

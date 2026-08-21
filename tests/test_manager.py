import pytest
from manager import TaskManager
from models import Task, TaskPriority, TaskStatus
from exceptions import EmptyTitleError, TaskNotFoundError
from datetime import datetime


title = "Test Task"
priority = TaskPriority.HIGH.value
description = "This is a test task."

def test_add_task():
    task_manager = TaskManager()
    task_manager.add_task(title, priority, description)
    task_manager.add_task(title, priority)
    tasks = task_manager.get_tasks()
    assert len(tasks) == 2
    assert tasks[0].title == title
    assert tasks[0].priority == priority
    assert tasks[0].description == description
    assert tasks[0].status == TaskStatus.NOT_STARTED.value
    assert tasks[0].id == 1  # First task should have ID 1
    assert tasks[0].creation_date == datetime.today().strftime("%d-%m-%Y")  # Creation date should be set
    assert tasks[1].description is None  # Second task should have no description
    with pytest.raises(EmptyTitleError):
        task_manager.add_task("", priority, description)

def test_generate_next_id():
    task_manager = TaskManager()
    assert task_manager._generate_next_id() == 1
    task_manager.add_task(title, priority, description)
    assert task_manager._generate_next_id() == 2
    task_manager.remove_task(1)
    assert task_manager._generate_next_id() == 1

def test_get_tasks():
    task_manager = TaskManager()
    task_manager.add_task(title, priority, description)
    task_manager.add_task("Another task", priority)
    tasks = task_manager.get_tasks()
    assert tasks[0].title == title
    assert tasks[1].title == "Another task"

def test_remove_task():
    task_manager = TaskManager()
    task_manager.add_task(title, priority, description)
    task_manager.add_task("Another task", priority)
    task_manager.remove_task(1)
    assert len(task_manager.tasks) == 1
    assert task_manager.tasks[0].title == "Another task"

def test_modify_task_title():
    task_manager = TaskManager()
    task_manager.add_task(title, priority, description)
    task_manager.modify_task_title(1, "New title")
    assert task_manager.tasks[0].title == "New title"

def test_get_task_by_id():
    task_manager = TaskManager()
    task_manager.add_task(title, priority, description)
    task = task_manager.get_task_by_id(1)
    assert task.title == title
    assert task.priority == priority
    assert task.description == description
    with pytest.raises(TaskNotFoundError):
        task_manager.get_task_by_id(999)  # Non-existent task ID should raise TaskNotFoundError

def test_finish_task():
    task_manager = TaskManager()
    task_manager.add_task(title, priority, description)
    task_manager.finish_task(1)
    task = task_manager.get_task_by_id(1)
    assert task.status == TaskStatus.DONE.value
    with pytest.raises(TaskNotFoundError):
        task_manager.finish_task(999)  # Non-existent task ID should raise TaskNotFoundError

def test_filter_tasks_by_done_status():
    task_manager = TaskManager()
    task_manager.add_task(title, priority, description)
    task_manager.add_task("Another Task", TaskPriority.MEDIUM.value)
    task_manager.finish_task(1)  # Mark the first task as done
    done_tasks = task_manager.filter_tasks_by_done_status(TaskStatus.DONE.value)
    not_started_tasks = task_manager.filter_tasks_by_done_status(TaskStatus.NOT_STARTED.value)
    assert len(done_tasks) == 1
    assert done_tasks[0].id == 1
    assert len(not_started_tasks) == 1
    assert not_started_tasks[0].id == 2
    assert len(task_manager.filter_tasks_by_done_status(None)) == 2
    assert task_manager.filter_tasks_by_done_status(None)[0].title == title
    assert task_manager.filter_tasks_by_done_status(None)[1].title == "Another Task"

def test_filter_tasks_by_priority():
    task_manager = TaskManager()
    task_manager.add_task(title, priority, description)
    task_manager.add_task("Another Task", TaskPriority.MEDIUM.value)
    high_priority_tasks = task_manager.filter_tasks_by_priority(TaskPriority.HIGH.value)
    medium_priority_tasks = task_manager.filter_tasks_by_priority(TaskPriority.MEDIUM.value)
    assert len(high_priority_tasks) == 1
    assert high_priority_tasks[0].id == 1
    assert len(medium_priority_tasks) == 1
    assert medium_priority_tasks[0].id == 2

def test_change_task_status():
    task_manager = TaskManager()
    task_manager.add_task(title, priority, description)
    task_manager.change_task_status(1, TaskStatus.IN_PROGRESS.value)
    task = task_manager.get_task_by_id(1)
    assert task.status == TaskStatus.IN_PROGRESS.value

def test_change_task_priority():
    task_manager = TaskManager()
    task_manager.add_task(title, priority, description)
    task_manager.change_task_priority(1, TaskPriority.MEDIUM.value)
    task = task_manager.get_task_by_id(1)
    assert task.priority == TaskPriority.MEDIUM.value
import pytest
from models import Task, TaskStatus, TaskPriority
from exceptions import InvalidPriorityError, InvalidStatusError


id = 0
title = "Test Task"
creation_date = "2023-10-01"
priority = TaskPriority.HIGH.value
description = "This is a test task."
status = TaskStatus.NOT_STARTED.value
new_title = "Modified Task Title"

def test_task_initialization():
    task = Task(id, title, creation_date, priority, description, status)
    assert task.id == id
    assert task.title == title
    assert task.creation_date == creation_date
    assert task.priority == priority
    assert task.description == description
    assert task.status == status

def test_mark_task_as_done():
    task = Task(id, title, creation_date, priority, description, status)
    task.mark_as_done()
    assert task.status == TaskStatus.DONE.value

def test_modify_task_title():
    task = Task(id, title, creation_date, priority, description, status)
    task.modify_title(new_title)
    assert task.title == new_title


def test_task_to_dict():
    task = Task(id, title, creation_date, priority, description, status)
    task_dict = task.to_dict()
    assert task_dict['id'] == id
    assert task_dict['title'] == title
    assert task_dict['creation_date'] == creation_date
    assert task_dict['priority'] == priority
    assert task_dict['description'] == description
    assert task_dict['status'] == status

def test_task_from_dict():
    task_data = {
        'id': id,
        'title': title,
        'creation_date': creation_date,
        'priority': priority,
        'description': description,
        'status': status
    }
    new_task = Task.from_dict(task_data)
    assert new_task.id == id
    assert new_task.title == title
    assert new_task.creation_date == creation_date
    assert new_task.priority == priority
    assert new_task.description == description
    assert new_task.status == status

def test_priority_transform():
    assert TaskPriority._priority_transform("1") == TaskPriority.HIGH
    assert TaskPriority._priority_transform("2") == TaskPriority.MEDIUM
    assert TaskPriority._priority_transform("3") == TaskPriority.LOW
    with pytest.raises(InvalidPriorityError):
        TaskPriority._priority_transform("invalid")

def test_status_transform():
    assert TaskStatus._status_transform("1") == TaskStatus.NOT_STARTED
    assert TaskStatus._status_transform("2") == TaskStatus.IN_PROGRESS
    assert TaskStatus._status_transform("3") == TaskStatus.DONE
    with pytest.raises(InvalidStatusError):
        TaskStatus._status_transform("invalid")
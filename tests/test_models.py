import pytest
from models import Task, TaskStatus, TaskPriority

id = 0
title = "Test Task"
creation_date = "2023-10-01"
priority = TaskPriority.HIGH.value
description = "This is a test task."
status = TaskStatus.NOT_STARTED.value
new_title = "Modified Task Title"

task = Task(id, title, creation_date, priority, description, status)

def test_mark_task_as_done():
    task.mark_as_done()
    assert task.status == TaskStatus.DONE.value

def test_modify_task_title():

    task.modify_title(new_title)
    assert task.title == new_title


def test_task_to_dict():
    task_dict = task.to_dict()
    assert task_dict['id'] == id
    assert task_dict['title'] == new_title
    assert task_dict['creation_date'] == creation_date
    assert task_dict['priority'] == priority
    assert task_dict['description'] == description
    assert task_dict['status'] == TaskStatus.DONE.value

def test_task_from_dict():
    task_data = {
        'id': id,
        'title': new_title,
        'creation_date': creation_date,
        'priority': priority,
        'description': description,
        'status': TaskStatus.DONE.value
    }
    new_task = Task.from_dict(task_data)
    assert new_task.id == id
    assert new_task.title == new_title
    assert new_task.creation_date == creation_date
    assert new_task.priority == priority
    assert new_task.description == description
    assert new_task.status == TaskStatus.DONE.value



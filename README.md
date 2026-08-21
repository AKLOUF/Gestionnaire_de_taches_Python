# Task Manager (CLI)

A command-line task manager built in Python to practice core language fundamentals: OOP, custom exceptions, JSON persistence, and unit testing with `pytest`.

## Features

- **Add a task** — title (required), priority, and an optional description. Empty titles are rejected.
- **Display all tasks** — shows ID, title, priority, and status for every task.
- **Filter tasks by priority** — `low`, `medium`, or `high`.
- **Filter tasks by status** — `not started`, `in progress`, or `done`.
- **Mark a task as done**.
- **Modify a task's title, priority, or status** — by ID.
- **Delete a task** — by ID.
- **Persistence** — tasks are automatically loaded from `data/backup.json` on startup and saved back to it on exit.
- **Input validation** — invalid menu choices, non-numeric IDs, invalid priority/status choices, and empty titles are all caught and reported without crashing the app.

## Project structure

```
Gestionnaire_de_taches_Python/
├── app/
│   ├── main.py         # Entry point
│   ├── cli.py           # Menu loop and user interaction
│   ├── manager.py       # TaskManager: business logic (add/remove/filter/modify tasks)
│   ├── models.py        # Task class, TaskPriority/TaskStatus enums
│   ├── storage.py       # save_tasks() / return_tasks(): JSON read/write
│   └── exceptions.py    # Custom exceptions
├── data/
│   └── backup.json      # Persisted tasks
├── tests/
│   ├── conftest.py
│   ├── test_models.py
│   ├── test_manager.py
│   └── test_storage.py
└── README.md
```

## Data model

Each task has:

| Field           | Type  | Description                          |
|-----------------|-------|---------------------------------------|
| `id`            | int   | Unique, auto-generated                |
| `title`         | str   | Required, cannot be empty             |
| `creation_date` | str   | Set automatically (`dd-mm-yyyy`)      |
| `priority`      | str   | `low`, `medium`, or `high`            |
| `description`   | str   | Optional                              |
| `status`        | str   | `not started`, `in progress`, `done`  |

## Custom exceptions

Defined in `app/exceptions.py` and used throughout `manager.py`/`models.py` instead of generic errors:

- `EmptyTitleError` — raised when a task title is empty.
- `TaskNotFoundError` — raised when a given task ID doesn't exist.
- `InvalidPriorityError` — raised when a priority choice isn't `1`, `2`, or `3`.
- `InvalidStatusError` — raised when a status choice isn't `1`, `2`, or `3`.

All are caught in `cli.py` and shown as clear messages instead of crashing the program.

## Installation

```bash
git clone https://github.com/AKLOUF/Gestionnaire_de_taches_Python
cd Gestionnaire_de_taches_Python
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install pytest
```

## Usage

Run from inside the `app/` directory:

```bash
cd app
python3 main.py
```

You'll get a numbered menu (1–10) to add, view, filter, modify, or delete tasks, and to quit (which automatically saves your tasks).

## Running the tests

From the project root:

```bash
pytest
```

The test suite (24 tests) covers:
- `test_models.py` — `Task` creation, `mark_as_done`, `modify_title`, `to_dict`/`from_dict`, and priority/status conversion (valid and invalid input).
- `test_manager.py` — adding, removing, retrieving, filtering, and modifying tasks, ID generation, and error cases (`EmptyTitleError`, `TaskNotFoundError`).
- `test_storage.py` — saving/loading tasks to/from JSON, including empty lists, missing files, invalid JSON, and invalid write paths. Tests use `pytest`'s `tmp_path` fixture so the real `data/backup.json` is never touched.

## Possible improvements

- Sort tasks by creation date or search by keyword.
- Add due dates and task categories.
- Persist to SQLite instead of JSON.
- Add a web interface (Flask/FastAPI) or REST API.

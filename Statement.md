# Problem statement

Students and small study groups often juggle assignments, revisions, and deadlines using scattered notes, sticky reminders, or simple text files. That fragmentation makes it easy to forget tasks, lose track of completed work, or waste time deciding what to do next. This project provides a lightweight, terminal-based Study To-Do List that makes it simple to add tasks, view the current list, and mark tasks done — keeping study work organized without requiring a full task-management system.

## Scope of the project

**In scope (current version):**

* In-memory task management using a single Python list (no persistence by default).
* Core operations: add task, view tasks, mark task as done.
* A clear, menu-driven CLI that runs in any terminal and uses `input()` prompts.
* Minimal, well-commented function-based code suitable for beginners and quick demos.

**Out of scope (can be added later):**

* Persistent storage (saving to JSON/CSV/SQLite).
* Task editing, deletion, or reordering (beyond marking done).
* Rich metadata for tasks (due dates, priorities, tags, subtasks, or assignees).
* Multi-user sync, networked features, or a graphical/web UI.
* Automated reminders, scheduling, or integrations with calendar services.

## Target users

* Individual students who want a simple CLI tool to track study tasks.
* Teachers or tutors creating small practice setups or demos.
* Beginner Python learners practicing I/O, lists, and simple program structure.
* Developers looking for a minimal starting point to extend into a larger task manager.

## High-level features

* **Add Task:** Prompt the user to type a task description and append it to the in-memory list.
* **View Tasks:** Print a numbered list of all tasks; shows a friendly message when no tasks exist.
* **Mark Task as Done:** Let the user choose a task by number and append a done marker (✔️), with basic input validation.
* **Simple CLI Flow:** A concise menu (Add / View / Mark Done / Exit) with clear prompts and feedback messages for ease of use.
* **Beginner-Friendly Code:** Function-separated logic (`add_task`, `view_tasks`, `mark_done`, `main`) that’s easy to read, test, and refactor.

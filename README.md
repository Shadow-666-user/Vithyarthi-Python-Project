# **Simple Study To-Do List (Python CLI)**

## **Overview**

This is a lightweight command-line To-Do List application designed to help students manage their study tasks.
Users can add tasks, view the full list, and mark tasks as completed.
All data is stored in memory using a Python list, making the program simple, fast, and ideal for beginners learning Python fundamentals.

## **Features**

* Add a new study task
* View all tasks with numbering
* Mark any task as **Done** (✔️ will be added)
* Simple menu-driven interface
* Beginner-friendly, clean function-based structure

## **Technologies / Tools Used**

* **Language:** Python 3.x
* **Standard Library:** No external libraries required
* Runs on any system with Python installed

## **Installation & Setup**

1. Install **Python 3.x**:

   * Windows/macOS: download from [https://www.python.org](https://www.python.org)
   * Linux: `sudo apt install python3`
2. Download or copy the project file:

   * `study_todo.py`
3. (Optional) Create a virtual environment if you want to isolate dependencies:

   ```
   python -m venv venv
   source venv/bin/activate   # macOS / Linux
   venv\Scripts\activate      # Windows
   ```

## **How to Run**

Open a terminal/command prompt and run:

```
python study_todo.py
```

You will see a menu like:

```
===== Study To-Do List =====
1. Add Task
2. View Tasks
3. Mark Task as Done
4. Exit
Choose (1-4):
```

Follow the prompts to add, view, or update tasks.

---

## **Example Usage**

### **Adding a Task**

```
Choose (1-4): 1
Enter task: Complete math homework
Task added!
```

### **Viewing Tasks**

```
Your Tasks:
1. Complete math homework
2. Read science chapter 4
```

### **Marking a Task as Done**

```
Choose (1-4): 3
Your Tasks:
1. Complete math homework
2. Read science chapter 4
Enter task number to mark done: 2
Marked as done!
```

Result:

```
1. Complete math homework
2. Read science chapter 4 ✔️
```

---

## **Input Format**

* Tasks are simple text strings.
* For marking tasks, enter a valid **task number** as shown in the list.
* Invalid numbers or non-numeric input will show an error message.

---

## **Testing**

### **Manual Tests**

* **Test A:** Add a new task and verify it shows in *View Tasks*.
* **Test B:** Mark a task as done and confirm ✔️ appears.
* **Test C:** Try marking a non-existent task number (e.g., `5` when only 2 tasks exist).
* **Test D:** View tasks when list is empty — program should say *"No tasks yet."*
* **Test E:** Try invalid input (letters instead of numbers).

### **Automated Testing Suggestions**

To automate tests:

* Refactor functions to accept parameters instead of using `input()`
* Use `pytest` to test:

  * `test_add_task()`
  * `test_view_tasks()`
  * `test_mark_done_valid()`
  * `test_mark_done_invalid_number()`

---

## **Suggested Improvements**

* Add option to delete tasks
* Add priority levels (High / Medium / Low)
* Save tasks to a file (JSON or text)
* Add a timestamp for each task
* Implement categories (Assignments, Revision, Projects, etc.)
* Add a GUI with Tkinter or a simple web UI with Flask

---

If you want, I can also **generate a PDF or DOCX version** of this README.

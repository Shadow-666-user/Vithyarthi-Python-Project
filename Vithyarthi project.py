tasks = []
def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added!\n")

def view_tasks():
    if len(tasks) == 0:
        print("No tasks yet.\n")
        return
    
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
    print()

def mark_done():
    if len(tasks) == 0:
        print("No tasks to update.\n")
        return
    
    view_tasks()
    try:
        num = int(input("Enter task number to mark done: "))
        tasks[num - 1] = tasks[num - 1] + " ✔️"
        print("Marked as done!\n")
    except:
        print("Invalid input.\n")

def main():
    while True:
        print("===== Study To-Do List =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Exit")

        choice = input("Choose (1-4): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.\n")

main()

import json

# ---------- Load tasks from file ----------
def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except:
        return {}

# ---------- Save tasks to file ----------
def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

# ---------- Add Task ----------
def add_task(tasks):
    task = input("Enter task: ")
    
    if tasks:
        new_id = str(int(max(tasks.keys())) + 1)
    else:
        new_id = "1"
    
    tasks[new_id] = {"task": task, "done": False}
    print("Task added!")

# ---------- Show Tasks ----------
def show_tasks(tasks):
    if not tasks:
        print("No tasks found!")
        return

    for key, value in tasks.items():
        status = "DONE" if value["done"] else "NOT DONE"
        print(key, ".", value["task"], "[", status, "]")

# ---------- Mark Done ----------
def mark_done(tasks):
    task_id = input("Enter task ID to mark done: ")

    if task_id in tasks:
        tasks[task_id]["done"] = True
        print("Task marked as done!")
    else:
        print("Invalid ID!")

# ---------- Remove Task ----------
def remove_task(tasks):
    task_id = input("Enter task ID to remove: ")

    if task_id in tasks:
        del tasks[task_id]
        print("Task removed!")
    else:
        print("Invalid ID!")

# ---------- Main Program ----------
def main():
    tasks = load_tasks()

    while True:
        print("\n--- TO DO LIST ---")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Done")
        print("4. Remove Task")
        print("5. Save & Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            remove_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Saved! Exiting...")
            break
        else:
            print("Invalid choice!")

# Run program
main()
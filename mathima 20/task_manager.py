tasks = []


def add_task(task_name):
    tasks.append({"name": task_name, "completed": False})


def mark_task_completed(task_name):
    for task in tasks:
        if task["name"] == task_name:
            task["completed"] = True
            return True
        return False


def list_task():
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for task in tasks:
            status = "Completed" if task["completed"] else "Not Completed"
            print(f"- {task['name']} ({status})")


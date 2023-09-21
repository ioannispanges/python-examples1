import task_manager


def main_task():
    print("Task Manager")
    print("------------")

    while True:
        print("\nMenu:")
        print("1. Add task")
        print("2. Mark task as completed")
        print("3. List tasks")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            task_name = input("Enter task name: ")
            task_manager.add_task(task_name)
            print(f"Task '{task_name}' added.")

        elif choice == '2':
            task_name = input("Enter task name to mark as completed: ")
            if task_manager.mark_task_completed(task_name):
                print(f"Task '{task_name}' marked as completed. ")
            else:
                print(f"Task '{task_name}' not found. ")

        elif choice == '3':
            task_manager.list_task()

        elif choice == '4':
            print("Thank you for using the Task Manager!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main_task()

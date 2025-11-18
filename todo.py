
---

## 🟦 **todo.py**
```python
# To-Do List Manager
# Uses Python LIST to store and manage tasks

tasks = []

while True:
    print("\n===== TO-DO LIST MANAGER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task to add: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        print("\nYour Tasks:")
        for idx, t in enumerate(tasks, start=1):
            print(f"{idx}. {t}")

    elif choice == "3":
        task = input("Enter task to remove: ")
        if task in tasks:
            tasks.remove(task)
            print("Task removed!")
        else:
            print("Task not found!")

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")

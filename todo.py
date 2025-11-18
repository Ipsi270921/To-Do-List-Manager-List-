"""
To-Do List Manager
------------------------------------
Features:
1. Add a task
2. View all tasks
3. Remove a task by NUMBER
4. Exit the program

Why this version is better?
- Users no longer need to type the exact task name.
- Removing tasks by number is simple and user-friendly.
- Prevents mistakes caused by spelling errors.
"""

# List to store tasks
tasks = []

while True:
    print("\n===== TO-DO LIST MANAGER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # -----------------------------
    # OPTION 1 → ADD TASK
    # -----------------------------
    if choice == "1":
        task = input("Enter task to add: ")
        tasks.append(task)  # Append task to list
        print("✔ Task added successfully!")

    # -----------------------------
    # OPTION 2 → VIEW TASKS
    # -----------------------------
    elif choice == "2":
        print("\nYour Tasks:")

        # If no tasks exist
        if len(tasks) == 0:
            print("No tasks added yet.")
        else:
            # Display tasks with numbering
            for idx, t in enumerate(tasks, start=1):
                print(f"{idx}. {t}")

    # -----------------------------
    # OPTION 3 → REMOVE TASK BY NUMBER
    # -----------------------------
    elif choice == "3":
        # If no tasks exist, cannot remove
        if len(tasks) == 0:
            print("\nNo tasks available to remove!")
            continue

        print("\nYour Tasks:")
        # Show tasks with numbers
        for idx, t in enumerate(tasks, start=1):
            print(f"{idx}. {t}")

        # Ask the user for the task number
        try:
            num = int(input("Enter task number to remove: "))

            # Check if number is valid
            if 1 <= num <= len(tasks):
                removed_task = tasks.pop(num - 1)  # pop removes by index
                print(f"✔ Task removed: {removed_task}")
            else:
                print("✘ Invalid task number. Try again!")

        except ValueError:
            print("✘ Please enter a valid NUMBER!")

    # -----------------------------
    # OPTION 4 → EXIT
    # -----------------------------
    elif choice == "4":
        print("👋 Exiting the program. Goodbye!")
        break

    else:
        print("✘ Invalid choice! Please select 1, 2, 3, or 4.")

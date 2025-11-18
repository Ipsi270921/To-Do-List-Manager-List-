"""
TO-DO LIST MANAGER (Remove by Number)
-------------------------------------
Features:
- Add tasks
- View tasks
- Remove tasks by selecting task NUMBER (1, 2, 3…)
- Handles invalid inputs gracefully
- Uses pop(index) so it NEVER shows "task not found"
"""

# -----------------------------
# Initialize empty task list
# -----------------------------
tasks = []


def show_tasks():
    """
    Print all tasks with index numbers.
    If no tasks exist, display a message.
    """
    if not tasks:
        print("No tasks available.")
        return

    print("\nYour Tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


# -----------------------------
# MAIN PROGRAM LOOP
# -----------------------------
while True:
    # Menu
    print("\n===== TO-DO LIST New MANAGER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task (by number)")
    print("4. Exit")

    # Get user choice
    choice = input("Enter your choice: ").strip()

    # -------------------------
    # OPTION 1: ADD TASK
    # -------------------------
    if choice == "1":
        task = input("Enter new task: ").strip()

        if task:   # avoid empty tasks
            tasks.append(task)
            print("✔ Task added!")
        else:
            print("✘ Cannot add an EMPTY task.")

    # -------------------------
    # OPTION 2: VIEW TASKS
    # -------------------------
    elif choice == "2":
        show_tasks()

    # -------------------------
    # OPTION 3: REMOVE TASK BY NUMBER
    # -------------------------
    elif choice == "3":
        if not tasks:
            print("✘ No tasks to remove.")
            continue

        show_tasks()

        # Ask for number
        user_input = input("Enter task number to remove: ").strip()

        # Validate number
        try:
            task_num = int(user_input)  # convert to int

            # Check valid range
            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)  # remove using index
                print(f"✔ Removed task: {removed}")
            else:
                print(f"✘ Invalid number! Choose between 1 and {len(tasks)}.")

        except ValueError:
            print("✘ Please enter a VALID NUMBER (like 1, 2, 3).")

    # -------------------------
    # OPTION 4: EXIT PROGRAM
    # -------------------------
    elif choice == "4":
        print("👋 Exiting... Have a great day!")
        break

    # -------------------------
    # INVALID MENU OPTION
    # -------------------------
    else:
        print("✘ Invalid choice! Please enter 1, 2, 3, or 4.")

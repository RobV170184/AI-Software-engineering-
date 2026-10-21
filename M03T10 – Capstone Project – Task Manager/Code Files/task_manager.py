#  Importing external modules 
from datetime import datetime, date


#  Helper: load data from files 

def load_users():
    """Read user.txt and return a dict of {username: password}."""
    user_dict = {}
    with open('user.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                username, password = line.split(', ', 1)
                user_dict[username] = password
    return user_dict


def load_tasks():
    """Read tasks.txt and return a list of task dicts."""
    tasks = []
    with open('tasks.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(', ')
            if len(parts) == 6:
                tasks.append({
                    'username': parts[0],
                    'title': parts[1],
                    'description': parts[2],
                    'assigned_date': parts[3],
                    'due_date': parts[4],
                    'completed': parts[5]
                })
    return tasks


def save_tasks(tasks):
    """Write the tasks list back to tasks.txt."""
    with open('tasks.txt', 'w') as f:
        for i, t in enumerate(tasks):
            line = (f"{t['username']}, {t['title']}, {t['description']}, "
                    f"{t['assigned_date']}, {t['due_date']}, {t['completed']}")
            if i < len(tasks) - 1:
                f.write(line + '\n')
            else:
                f.write(line)


def format_task(task):
    """Return a formatted string representation of a task."""
    return (
        f"\nTask:               {task['title']}\n"
        f"Assigned to:        {task['username']}\n"
        f"Date assigned:      {task['assigned_date']}\n"
        f"Due date:           {task['due_date']}\n"
        f"Task Complete?      {task['completed']}\n"
        f"Task description:\n  {task['description']}\n"
        f"{'-' * 60}"
    )


#  Part 3 Functions 

def reg_user(user_dict):
    """Register a new user and save to user.txt (admin only)."""
    while True:
        new_username = input("Enter new username: ").strip()
        if new_username in user_dict:
            print("Error: That username already exists. Please try a different one.")
            continue

        new_password = input("Enter new password: ").strip()
        confirm_password = input("Confirm password: ").strip()

        if new_password != confirm_password:
            print("Passwords do not match. Please try again.")
            continue

        user_dict[new_username] = new_password
        with open('user.txt', 'a') as f:
            f.write(f"\n{new_username}, {new_password}")
        print("User registered successfully!")
        break


def add_task(user_dict):
    """Prompt for task details and append to tasks.txt."""
    while True:
        task_username = input("Username of person assigned to task: ").strip()
        if task_username not in user_dict:
            print("Error: That user does not exist. Please enter a valid username.")
            continue
        break

    task_title = input("Title of task: ").strip()
    task_description = input("Description of task: ").strip()

    while True:
        task_due_date = input("Due date of task (e.g., 10 Oct 2019): ").strip()
        try:
            datetime.strptime(task_due_date, "%d %b %Y")
            break
        except ValueError:
            print("Invalid date format. Please use DD Mon YYYY (e.g., 10 Oct 2019).")

    current_date = datetime.now().strftime("%d %b %Y")

    with open('tasks.txt', 'a') as f:
        f.write(f"\n{task_username}, {task_title}, {task_description}, "
                f"{current_date}, {task_due_date}, No")
    print("Task added successfully!")


def view_all():
    """Display all tasks in a user-friendly format."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    print("\n" + "=" * 60)
    print("ALL TASKS")
    print("=" * 60)
    for task in tasks:
        print(format_task(task))


def get_valid_task_number(num_tasks):
    """Recursively prompt until the user enters a valid task number or -1."""
    try:
        selection = int(input(f"Enter a task number (1-{num_tasks}) or -1 to return: "))
        if selection == -1:
            return -1
        if 1 <= selection <= num_tasks:
            return selection
        print(f"Invalid number. Please enter a value between 1 and {num_tasks}.")
    except ValueError:
        print("Invalid input. Please enter a whole number.")
    return get_valid_task_number(num_tasks)


def view_mine(current_user):
    """Display tasks for the current user with options to edit or complete."""
    tasks = load_tasks()
    my_tasks = [(i, t) for i, t in enumerate(tasks) if t['username'] == current_user]

    if not my_tasks:
        print("You have no tasks assigned.")
        return

    print("\n" + "=" * 60)
    print(f"TASKS FOR {current_user}")
    print("=" * 60)
    for num, (_, task) in enumerate(my_tasks, start=1):
        print(f"\nTask {num}:{format_task(task)}")

    selection = get_valid_task_number(len(my_tasks))
    if selection == -1:
        return

    original_index, chosen_task = my_tasks[selection - 1]

    if chosen_task['completed'] == 'Yes':
        print("This task is already completed and cannot be edited.")
        return

    action = input("Choose action:\n  c - mark as complete\n  e - edit task\n: ").lower().strip()

    if action == 'c':
        tasks[original_index]['completed'] = 'Yes'
        save_tasks(tasks)
        print("Task marked as complete.")

    elif action == 'e':
        print("What would you like to edit?")
        edit_choice = input("  u - change assigned user\n  d - change due date\n  b - both\n: ").lower().strip()

        if edit_choice in ('u', 'b'):
            user_dict = load_users()
            while True:
                new_user = input("Enter new username to assign task to: ").strip()
                if new_user in user_dict:
                    tasks[original_index]['username'] = new_user
                    break
                print("User does not exist. Please enter a valid username.")

        if edit_choice in ('d', 'b'):
            while True:
                new_due = input("Enter new due date (e.g., 10 Oct 2019): ").strip()
                try:
                    datetime.strptime(new_due, "%d %b %Y")
                    tasks[original_index]['due_date'] = new_due
                    break
                except ValueError:
                    print("Invalid date format. Please use DD Mon YYYY.")

        save_tasks(tasks)
        print("Task updated successfully.")
    else:
        print("Invalid option. Returning to menu.")


def view_completed():
    """Display only tasks that have been marked as complete (admin only)."""
    tasks = load_tasks()
    completed = [t for t in tasks if t['completed'] == 'Yes']
    if not completed:
        print("No completed tasks found.")
        return
    print("\n" + "=" * 60)
    print("COMPLETED TASKS")
    print("=" * 60)
    for task in completed:
        print(format_task(task))


def delete_task():
    """Display all tasks and allow admin to delete one by number."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks to delete.")
        return

    print("\n" + "=" * 60)
    print("DELETE A TASK")
    print("=" * 60)
    for i, task in enumerate(tasks, start=1):
        print(f"\nTask {i}:{format_task(task)}")

    selection = get_valid_task_number(len(tasks))
    if selection == -1:
        return

    removed = tasks.pop(selection - 1)
    save_tasks(tasks)
    print(f"Task '{removed['title']}' deleted successfully.")


def generate_reports():
    """Generate task_overview.txt and user_overview.txt."""
    tasks = load_tasks()
    user_dict = load_users()
    today = date.today()
    total_tasks = len(tasks)

    # ---- task_overview.txt ----
    completed_tasks = sum(1 for t in tasks if t['completed'] == 'Yes')
    uncompleted_tasks = total_tasks - completed_tasks

    overdue_tasks = 0
    for t in tasks:
        if t['completed'] == 'No':
            try:
                due = datetime.strptime(t['due_date'], "%d %b %Y").date()
                if due < today:
                    overdue_tasks += 1
            except ValueError:
                pass

    pct_incomplete = (uncompleted_tasks / total_tasks * 100) if total_tasks else 0
    pct_overdue = (overdue_tasks / total_tasks * 100) if total_tasks else 0

    with open('task_overview.txt', 'w') as f:
        f.write("===== Task Overview =====\n")
        f.write(f"Total tasks:                    {total_tasks}\n")
        f.write(f"Completed tasks:                {completed_tasks}\n")
        f.write(f"Uncompleted tasks:              {uncompleted_tasks}\n")
        f.write(f"Overdue (incomplete) tasks:     {overdue_tasks}\n")
        f.write(f"Percentage incomplete:          {pct_incomplete:.1f}%\n")
        f.write(f"Percentage overdue:             {pct_overdue:.1f}%\n")

    #  user_overview.txt 
    total_users = len(user_dict)

    with open('user_overview.txt', 'w') as f:
        f.write("===== User Overview =====\n")
        f.write(f"Total users:    {total_users}\n")
        f.write(f"Total tasks:    {total_tasks}\n\n")

        for username in user_dict:
            user_tasks = [t for t in tasks if t['username'] == username]
            u_total = len(user_tasks)
            u_completed = sum(1 for t in user_tasks if t['completed'] == 'Yes')
            u_incomplete = u_total - u_completed

            u_overdue = 0
            for t in user_tasks:
                if t['completed'] == 'No':
                    try:
                        due = datetime.strptime(t['due_date'], "%d %b %Y").date()
                        if due < today:
                            u_overdue += 1
                    except ValueError:
                        pass

            pct_of_total = (u_total / total_tasks * 100) if total_tasks else 0
            pct_u_completed = (u_completed / u_total * 100) if u_total else 0
            pct_u_incomplete = (u_incomplete / u_total * 100) if u_total else 0
            pct_u_overdue = (u_overdue / u_total * 100) if u_total else 0

            f.write(f"--- {username} ---\n")
            f.write(f"  Tasks assigned:             {u_total}\n")
            f.write(f"  % of all tasks:             {pct_of_total:.1f}%\n")
            f.write(f"  % completed:                {pct_u_completed:.1f}%\n")
            f.write(f"  % to still complete:        {pct_u_incomplete:.1f}%\n")
            f.write(f"  % overdue (incomplete):     {pct_u_overdue:.1f}%\n\n")

    print("Reports generated: task_overview.txt and user_overview.txt")


def display_statistics():
    """Display the contents of task_overview.txt and user_overview.txt."""
    import os
    if not os.path.exists('task_overview.txt') or not os.path.exists('user_overview.txt'):
        generate_reports()

    print("\n" + "=" * 60)
    with open('task_overview.txt', 'r') as f:
        print(f.read())

    print("=" * 60)
    with open('user_overview.txt', 'r') as f:
        print(f.read())


#  Login Section 

user_dict = load_users()

logged_in = False
current_user = ""

while not logged_in:
    print("LOGIN")
    username_input = input("Username: ").strip()
    password_input = input("Password: ").strip()

    if username_input not in user_dict:
        print("Error: Username not found. Please try again.")
    elif user_dict[username_input] != password_input:
        print("Error: Incorrect password. Please try again.")
    else:
        print("Login successful!")
        logged_in = True
        current_user = username_input


#  Main Menu 

while True:
    if current_user == 'admin':
        menu = input(
            '''\nPlease select one of the following options:
r - register user
a - add task
va - view all tasks
vm - view my tasks
vc - view completed tasks
del - delete a task
ds - display statistics
gr - generate reports
e - exit
: '''
        ).lower().strip()
    else:
        menu = input(
            '''\nPlease select one of the following options:
a - add task
va - view all tasks
vm - view my tasks
e - exit
: '''
        ).lower().strip()

    if menu == 'r':
        if current_user != 'admin':
            print("Only admin can register users.")
        else:
            user_dict = load_users()
            reg_user(user_dict)
            user_dict = load_users()

    elif menu == 'a':
        user_dict = load_users()
        add_task(user_dict)

    elif menu == 'va':
        view_all()

    elif menu == 'vm':
        view_mine(current_user)

    elif menu == 'vc':
        if current_user != 'admin':
            print("Only admin can view completed tasks.")
        else:
            view_completed()

    elif menu == 'del':
        if current_user != 'admin':
            print("Only admin can delete tasks.")
        else:
            delete_task()

    elif menu == 'ds':
        if current_user != 'admin':
            print("Only admin can display statistics.")
        else:
            display_statistics()

    elif menu == 'gr':
        if current_user != 'admin':
            print("Only admin can generate reports.")
        else:
            generate_reports()

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("Invalid option. Please try again.")

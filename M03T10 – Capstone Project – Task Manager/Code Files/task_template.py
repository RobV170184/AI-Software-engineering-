# ===== Importing external modules ===========
from datetime import datetime

# ==== Login Section ====
# Read usernames and passwords from user.txt file
user_dict = {}
with open('user.txt', 'r') as file:
    for line in file:
        username, password = line.strip().split(', ')
        user_dict[username] = password

# Use a while loop to validate username and password
logged_in = False
current_user = ""

while not logged_in:
    print("LOGIN")
    username_input = input("Username: ")
    password_input = input("Password: ")

    if username_input in user_dict and user_dict[username_input] == password_input:
        print("Login successful!")
        logged_in = True
        current_user = username_input
    else:
        print("Invalid username or password. Please try again.")

# ==== Main Menu ====

while True:
    # Present the menu to the user and
    # make sure that the user input is converted to lower case.
    menu = input(
        '''Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
e - exit
: '''
    ).lower()

    if menu == 'r':
        # Register a new user
        new_username = input("Enter new username: ")
        new_password = input("Enter new password: ")
        confirm_password = input("Confirm password: ")

        if new_password == confirm_password:
            # Add to dictionary
            user_dict[new_username] = new_password
            # Write to file
            with open('user.txt', 'a') as file:
                file.write(f"\n{new_username}, {new_password}")
            print("User registered successfully!")
        else:
            print("Passwords do not match. User not registered.")

    elif menu == 'a':
        # Add a new task
        task_username = input("Username of person assigned to task: ")
        task_title = input("Title of task: ")
        task_description = input("Description of task: ")
        task_due_date = input("Due date of task (e.g., 10 Oct 2019): ")

        # Get current date
        current_date = datetime.now().strftime("%d %b %Y")

        # Write to tasks.txt file
        with open('tasks.txt', 'a') as file:
            file.write(f"\n{task_username}, {task_title}, {task_description}, {current_date}, {task_due_date}, No")
        print("Task added successfully!")

    elif menu == 'va':
        # View all tasks
        print("\n" + "="*60)
        print("ALL TASKS")
        print("="*60)

        with open('tasks.txt', 'r') as file:
            for line in file:
                task_data = line.strip().split(', ')
                if len(task_data) == 6:
                    username, title, description, assigned_date, due_date, completed = task_data
                    print(f"\nTask:               {title}")
                    print(f"Assigned to:        {username}")
                    print(f"Date assigned:      {assigned_date}")
                    print(f"Due date:           {due_date}")
                    print(f"Task Complete?      {completed}")
                    print(f"Task description:\n  {description}")
                    print("-" * 60)

    elif menu == 'vm':
        # View my tasks
        print("\n" + "="*60)
        print(f"TASKS FOR {current_user}")
        print("="*60)

        task_found = False
        with open('tasks.txt', 'r') as file:
            for line in file:
                task_data = line.strip().split(', ')
                if len(task_data) == 6:
                    username, title, description, assigned_date, due_date, completed = task_data
                    # Check if task belongs to current user
                    if username == current_user:
                        task_found = True
                        print(f"\nTask:               {title}")
                        print(f"Assigned to:        {username}")
                        print(f"Date assigned:      {assigned_date}")
                        print(f"Due date:           {due_date}")
                        print(f"Task Complete?      {completed}")
                        print(f"Task description:\n  {description}")
                        print("-" * 60)

        if not task_found:
            print("You have no tasks assigned.")

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have entered an invalid input. Please try again")
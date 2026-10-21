"""
Email Simulator Program

This program demonstrates OOP concepts by creating an email simulator
with Email objects that can be marked as read or unread.
"""

#  OOP Email Simulator  #

#  Email Class  #
class Email:

    # Constructor takes three arguments: email_address, subject_line, email_content
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False  # Initialised to False by default

    # Method to mark an email as read by setting has_been_read to True
    def mark_as_read(self):
        self.has_been_read = True


#  Lists  #
# Initialise an empty list to store the email objects.
inbox = []


#  Functions  #

def populate_inbox():
    # Create 3 sample emails and add them to the inbox list.
    email1 = Email("support@company.com", "Welcome to our service!",
                   "Thank you for signing up. We're excited to have you!")
    email2 = Email("newsletter@news.com", "Weekly Newsletter - Top Stories",
                   "Here are this week's top stories from around the world.")
    email3 = Email("friend@email.com", "Catch up soon?",
                   "Hey! It's been a while. Want to grab coffee sometime?")

    inbox.append(email1)
    inbox.append(email2)
    inbox.append(email3)


def list_emails():
    # Print each email's subject line alongside its corresponding index number.
    # Using enumerate() as recommended.
    print("\nEmail List:")
    for i, email in enumerate(inbox):
        print(f"{i}  {email.subject_line}")


def read_email(index):
    # Display the selected email's address, subject line, and content,
    # then mark it as read.
    email = inbox[index]
    print(f"\nFrom: {email.email_address}")
    print(f"Subject: {email.subject_line}")
    print(f"Content: {email.email_content}")
    email.mark_as_read()
    print(f"\nEmail from {email.email_address} marked as read.\n")


#  Email Program  #

# Populate the inbox with 3 sample emails at program start-up.
populate_inbox()

# Display the menu options for each iteration of the loop.
while True:
    user_choice = int(
        input(
            """\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: """
        )
    )

    if user_choice == 1:
        # List all emails and let the user choose one to read by index.
        list_emails()
        email_index = int(input("\nEnter the index of the email you want to read: "))
        read_email(email_index)

    elif user_choice == 2:
        # View unread emails - access subject_line directly (no separate function needed).
        print("\nUnread Emails:")
        unread_found = False
        for i, email in enumerate(inbox):
            if not email.has_been_read:
                print(f"{i}  {email.subject_line}")
                unread_found = True
        if not unread_found:
            print("No unread emails.")

    elif user_choice == 3:
        # Quit application.
        print("Goodbye!")
        break

    else:
        print("Oops - incorrect input.")

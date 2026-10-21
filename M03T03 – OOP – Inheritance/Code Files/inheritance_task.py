# --- Task 1: OOP Inheritance ---

class Course:
    # Class attribute for the course name
    name = "Fundamentals of Computer Science"

    # Class attribute for the contact website
    contact_website = "www.hyperiondev.com"

    # Method to display contact details
    def contact_details(self):
        print("Please contact us by visiting", self.contact_website)

    # Added method to print the head office location
    def head_office_location(self):
        print("Head office location: Cape Town")


# OOPCourse subclass inheriting from Course
class OOPCourse(Course):

    # Constructor with default values for description and trainer
    def __init__(self, description="OOP Fundamentals", trainer="Mr Anon A. Mouse"):
        self.description = description
        self.trainer = trainer

    # Method that prints what the course is about and the trainer's name
    def trainer_details(self):
        print(f"This course is about: {self.description}")
        print(f"Trainer: {self.trainer}")

    # Method that prints the course ID number
    def show_course_id(self):
        print("Course ID: #12345")


# Create an object of OOPCourse and call the required methods
course_1 = OOPCourse()
course_1.contact_details()
course_1.trainer_details()
course_1.show_course_id()

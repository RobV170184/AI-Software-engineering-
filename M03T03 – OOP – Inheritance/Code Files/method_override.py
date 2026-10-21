# --- Task 2: Method Overriding ---

# Take user inputs for name, age, hair colour, and eye colour
name = input("Enter name: ")
age = int(input("Enter age: "))
hair_colour = input("Enter hair colour: ")
eye_colour = input("Enter eye colour: ")


class Adult:
    """Parent class representing an adult person."""

    def __init__(self, name, age, eye_color, hair_color):
        self.name = name
        self.age = age
        self.eye_color = eye_color
        self.hair_color = hair_color

    def can_drive(self):
        print(f"{self.name} is old enough to drive.")


class Child(Adult):
    """Child subclass that inherits from Adult but overrides can_drive()."""

    # Inherits the same attributes from Adult via super()
    def __init__(self, name, age, eye_color, hair_color):
        super().__init__(name, age, eye_color, hair_color)

    # Override can_drive to indicate the person is too young to drive
    def can_drive(self):
        print(f"{self.name} is too young to drive.")


# Create an Adult instance if age >= 18, otherwise create a Child instance
if age >= 18:
    person = Adult(name, age, eye_colour, hair_colour)
else:
    person = Child(name, age, eye_colour, hair_colour)

# Call can_drive to print whether the person is old enough to drive
person.can_drive()

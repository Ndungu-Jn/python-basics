class Person:
    def __init__(self, name, age): #the constructor
        self.name = name  # Initializing the name attribute
        self.age = age    # Initializing the age attribute

    def display_info(self): #A function to  display
        print(f"Name: {self.name}, Age: {self.age}")

# Creating an instance of the Person class
person1 = Person("John", 24)


# Accessing attributes and methods
person1.display_info()

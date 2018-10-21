# Creating a class defining the dataset for this

class Student:
    def __init__(self, name, grade, gpa, is_a_bad_student): #initializing a student
        self.name = name
        self.grade = grade
        self.gpa = gpa
        self.is_a_bad_student = is_a_bad_student

    def on_honor_roll(self): #You can add functions to classes making them more dynamic or more specialized according to the dataset
        if self.gpa >= 3.5:
            return True
        else:
            return False

#Used for MultipleChoice game
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

class Chef:
    def make_chicken(self):
        print("The Chef makes chicken")
    def make_pasta(self):
        print("The chef makes pasta")
    def make_salad(self):
        print("The chef makes a salad")

class FrenchChef(Chef): #inheritance of the chef class above
    def make_chicken(self):
        print("The French chef will do a chicken a la orange")
    def make_baguette(self):
        print("The chef makes a baguette")
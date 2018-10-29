#testing importing other functions
import useful_tools
import docx # also installed python-docx contains a bunch of modules
# https://python-docx.readthedocs.io/en/latest/

print(useful_tools.roll_dice(7))

#https://docs.python.org/3/py-modindex.html list of python modules

from Classes import Student

student1 = Student("Jim", "Maths", 3.1, False) #student object, possible to access datatype created
student2 = Student("Pam", "Art", 2.6, True)
print(student1.name)
print(student2.gpa)
print(student1.on_honor_roll())

#importing from a certain class created playing with inheritance
from Classes import Chef
from Classes import FrenchChef

#Gives an error in code if the function defined doesnt exist
#assert hasattr(FrenchChef, 'make_baguette'), "This funcition doesnt exist!"

myChef = Chef()
myChef.make_pasta()
myFrenchChef = FrenchChef()
myFrenchChef.make_baguette()
myFrenchChef.make_chicken()
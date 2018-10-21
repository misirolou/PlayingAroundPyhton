#Try except statements to handle issues when needs be
try:
   # print(10/0) # this will give an error for dividing by zero
    number = int(input("Please add a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err) #prints out the actual error that happened
except ValueError:
    print("Invalid input")
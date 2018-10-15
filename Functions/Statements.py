# Statements around if, while, for loops, ...
print("Starting off with declaring the differnt types of statements availible in python")

is_male = True
is_tall = False

if is_male and is_tall: #starting a if statement, can use or, and, diff
    print("You are a man or tall")
    print("Adding line also works")
elif is_male and not(is_tall):
    print("you are a short man")
elif not(is_male) and is_tall:
    print("you are not a man that is tall")
else:                   # adding else statement
    print("You are a not a man or tall")

#comparing differnet values
print("------------comparing statements---------------")
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3: #conparing values ==, !=, >=, >, <, <=
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(5, 2, 4))
#Simple calculator with menu so users can choose to be used
num1 = float(input("Enter First number: ")) #forcing user to input a number
operator = input("Enter operator: ")
num2 = float(input("Enter second number: "))

#Different options for each operator
if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "/":
    print(num1 / num2)
elif operator == "*":
    print(num1 * num2)
else:
    print("Invalid opertor")
#Functions in python to organize things better
print("Starting with functions")

def say_hi(): # this is initializing the funcition
    print("Hello who are you?")

say_hi() #calling the function

name = input("Enter your name: ")
def say_hi_test(name):
    print("Hello " + name)

say_hi_test(name)

#Return statement
def return_test(num): 
    print("-------RETURN STATEMENT--------")
    return num*num*num
    print("Code") #doesn´t return due to return above exiting the function

result = return_test(4)
print(result)


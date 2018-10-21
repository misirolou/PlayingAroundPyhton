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

#Exponent functions
def raise_to_power(base_num, pow_num): #base number times base number, pow_num of times
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

#all the ways to do raise to the power options
print(raise_to_power(3, 4))
print(pow(3, 4)) #Exact same function as above, just playing around
print(2**3) # same as 2 * 2 * 2 or pow(2, 3), base num 2 and times 3

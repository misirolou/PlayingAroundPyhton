#This will contain necessary user input, to understand the basics
print("Learning how to add input from a User")

#getting input from user
print("Getting users input")
name = input("Enter your name: ")
age = input("What is your age: ")
print("Hello " + name + "!")  
print("You are " + age)

#building a calculator
print("Building a calculator")
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = float(num1) + float(num2)
print(result)

print("Adding an input with the amount of elements to go through")
n = int(input())

array = []
for eachN in range(1, n+1):
    array.append(eachN)

print(*array, sep='') #removes array brackets with * - unpacking the array, adding sep='' removes spaces between wach of the elements

#to split to various values received in this case its two, but can be more, add space to split each of the values
s, r = input().split()

print(s)
print(r)

#To group certain values with each other, for ex: input= 1222311, output = (1, 1) (3, 2) (1, 3) (2, 1)
from itertools import groupby #https://docs.python.org/2/library/itertools.html#itertools.groupby

s = input()
for i, j in groupby(s): 
    print((len(list(j)),int(i)),end=" ") #adding end seprates everything similar to \t and adding braces around len(list(j)), int(i) creates the braces around the info
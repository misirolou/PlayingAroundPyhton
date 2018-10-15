# print hello world, how every programmer starts
print("Hello  World")

#playing around with variables
character_name = "John"
character_age = 50

#converting int to string
s = str(character_age)
###### TRY IT OUT ######
print("There once was a man named " + character_name)
print("He was " + s + " years old")
print(character_name + " didn´t like his name and wanted to change")
print("He also wanted to be younger than " + s)

#Playing around with Strings
phrase = "what are penguins"
print("Giraffe \n\"have long necks\"")
print(phrase)
#Changing phrase string to upper case
print(phrase.upper() + "\tThey wear suits")
#Length of string
print(len(phrase))
#Indexing certain characters
print(phrase[0]) #should get w
#looking for characters in string to know index
print(phrase.index("a")) #should give an index num for that letter
#replacing certain words
print(phrase.replace("what", "how"))

#Playing around with numbers
print(20.0982)
print(3 + 4.1) #Can do all operations
print(3 * 4 + 5) 
print(10 % 3) #gives the remainder

my_num = 5
print(str(my_num) + "is a number") # converting to string
print(abs(-my_num)) # absolute value of number
print(pow(3, 2)) #same as 3 to power of 2
print(max(4, 5, 2, 1)) # 5 is the biggest
print(min(3, 1)) # 1 is the smallest
print(round(3.7)) # rounds number to 4
print(round(3.4)) # rounds number to 3

#trying different maths approaches
from math import *
print(floor(3.7)) #rounds number to lower case
print(ceil(3.7)) #rounds number to upper case
print(sqrt(12)) #does the square root of the number
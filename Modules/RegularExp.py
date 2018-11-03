#Regular expressions with re
'''
identifiers - different type of identifiers that can be used
\d = any number
\D = anything but a number
\s = space
\S = anything but a space
\w = any letter/character
\W = anything but a letter/character
. = any character, except for a new line
\b = space around whole words
\. = period. must use backslash, because . normally means any character.

Modifiers - what to modify
{1,3} = for digits, u expect 1-3 counts of digits, or "places"
+ = match 1 or more
? = match 0 or 1 repetitions.
* = match 0 or MORE repetitions
$ = matches at the end of string
^ = matches start of a string
| = matches either/or. Example x|y = will match either x or y
[] = range, or "variance"
{x} = expect to see the x amount of the preceding code.
{x,y} = expect to see this x-y amounts of the precedng code

White space characters:
\n = new line
\s = space
\t = tab
\e = escape
\f = form feed
\r = carriage return

Characters to REMEMBER TO ESCAPE IF USED!
. + * ? [ ] $ ^ ( ) { } | \
'''
import re

exampleString = '''
Jessica is 15 years ol and Daniel is 27 years old.
Edwards is 97, and his father, Oscar is 112 years.
'''

ages = re.findall(r'\d{1,3}', exampleString) #goes looking for all the numbers in the string contain 1 decimal - 3 decimal values
names = re.findall(r'[A-Z][a-z]*', exampleString) #looks for words that start with A-Z and inbetween until a whitespace, weird character appears

print(ages)
print(names)

ageDict = {}
x = 0
for eachName in names:
    ageDict[eachName] = ages[x]
    x+=1

print(ageDict)
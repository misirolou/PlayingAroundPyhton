#While loops in Python
num = 1
while num <= 10:
    print(num)
    num += 1

print("Done with while loop")

#For loops in Python
print("Through each of the letters in the string")
for letter in "Penguins look smart": #loops through each of the letters in the phrase
    print(letter)

print("To go through an array")
arrraytest = ["Jim", "Karen", "Kevin"]
len(arrraytest) #the length of the array
for name in arrraytest: #prints each of the names in the array
    print(name)

print("To go through a range of options")
for index in range(3, 11): #prints from 3 to 10
    print(index)

print("Testing if statements with range")
for i in range(5):
    if i is 1:
        print("I am number 1")
    else:
        print("I am not number 1")

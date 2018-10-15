#Lists 
players = ["Messi", "Ronaldo", "Pele", "Maradona"]
print(players) #prints list
print(players[2]) # prints Pele
print(players[-1]) # starts from the back using negative numbers
print(players[2:]) #prints Pele and Maradona
players.append("Neymar") # appends neymar to the end of the list
print(players)
print(players[1:3]) # From position 1 to 3, not adding num 3 info

print("------------------------------------------------------")
lucky_numbers = [4, 8, 15, 16, 23, 42]
People = ["Kevin", "karen", "Jim", "Oscar", "Tony"]
People.extend(lucky_numbers)
print(People) #Priniting list of people adding the numbers
People.append("Pedro") #adds to the end of the list
People.insert(2, "Kelly") #Kelly will be inserted to 2 position
People.remove("Jim") # removes Jim from the list
print(People)
People.pop() #removes last element from list
print(People.index("Tony"))
print(People.count("Kelly"))
lucky_numbers.sort() #Sorts the order of the list from smallest to biggest
print(lucky_numbers)
lucky_numbers.reverse() #Reverses order of list
print(lucky_numbers)
Friends = People.copy() #copies list that already exists


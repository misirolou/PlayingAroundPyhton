#2d lists and nest loops to play around with
print("Making a 2 dimentional list")
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 6, 8],
    [0]
]

print(number_grid[0]) #prints the row 
print(number_grid[1][1]) #prints the num assosciated to the row and column num (5)

for row in number_grid:
    for col in row:
        print(col)  #prints out each of the elements from the matrix
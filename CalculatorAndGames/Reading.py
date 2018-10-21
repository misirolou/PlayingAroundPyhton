#Reading from external files, very basic
 # r - read, w - write, a - append, r+ - read and write
 # w - also creates new file if it doesn´t exist or overwrites file
try:
    employee_file = open("employee.txt", "r") # r - read, w - write, a - append, r+ - read and write
    if employee_file.readable() is True: # verify if file is readable
        print(employee_file.readline()) # read the first line
        print(employee_file.readline()) # next line
        print(employee_file.readlines()) #adds info to a array
        #print(employee_file.read()) #read the entire file
    employee_file.close()
except FileNotFoundError as err:
    print(err)

#writing from the same file
print("Writing to the file created above")
employee_file_new = open("employee.txt", "a")
employee_file_new.write("\nRaphael - Dont mess with him")
employee_file_new.close()
#Dictionaries in general to understand how they work
#Dict{Key: Value} Key is always unique
monthConversion = {
    "Jan": "January",
    "Feb": "Febuary",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(monthConversion["Nov"]) #Gives the value for that key
#Gives the value for that key, contains default if key is invalid
print(monthConversion.get("Dec", "Not a valid a key")) 
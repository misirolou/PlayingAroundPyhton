#building a simple translator that changes certain words
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou": #same thing as "AEIOUaeiuo"
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))
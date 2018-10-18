#Playing around with a simple game that uses a bunch of functions
secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

print("This is an animal from africa, what am I?")
while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Guess the secret word: ")
        guess_count  += 1
    else:
        out_of_guesses = True

if out_of_guesses == True:
    print("You lose!")
else:
    print("You win!")

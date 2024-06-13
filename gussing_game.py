import random, sys


randomNumber = random.randint(1,20)
print("I am thinking of a number between 1 and 20.")
print("#DEBUG: " + str(randomNumber))
guessCount = 0
while True:
    print("Take a guess.")
    guess = input()
    guess = int(guess)
    guessCount = guessCount + 1

    if guess == randomNumber:
        print("Good job! You guessed my number in " + str(guessCount) + " guesses!")
        sys.exit()
    else:
        if guess < randomNumber:
            print("Your guess is too low.")
        else: print("Your guess is too high")

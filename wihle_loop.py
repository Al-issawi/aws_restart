#importing library 
import random

print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

#genarate random number from 1 to 10 .by using the random library.
number= random.randint(1, 10)

#loop variable 
isGuessRight = False

while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))        
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn't it. Try again.".format(guess))

        

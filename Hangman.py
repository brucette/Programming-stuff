#Hangman game
#computer picks random word and player tries to guess it one letter at a time. If they can't guess in time, the little stick figure gets hanged.

import random 

#Constants

HANGMAN = (
"""
------
|    |
|
|
|
|
|
|
|
----------
""",
"""
------
|    |
|    O
|
|
|
|
|
|
----------
""", 
"""
------
|    |
|    O
|   -+-
|
|
|
|
|
----------
""",
"""
------
|    |
|    O
|  /-+-
|  
|
|
|
|
----------
""",
""" 
------
|    |
|    O
|  /-+-/
|  
|
|
|
|
----------
""",
"""
------
|    |
|    O
|  /-+-/
|    |  
|
|
|
|
----------
""",
"""
------
|    |
|    O
|  /-+-/
|    |  
|    |
|   |
|   |
|
----------
""",
"""
------
|    |
|    O
|  /-+-/
|    |  
|    |
|   | |
|   | |
|
----------
""")

#Create constant to represent maximum number of guesses possible

MAX_WRONG = len(HANGMAN)-1

WORDS = ("OVERUSED","MUTABLE","CORNBREAD","INVISIBLE","JEALOUS","MOUNTAIN")

#Initialize variables
word = random.choice(WORDS)  #the word to be guessed

so_far = "-" * len(word)     #one dash for each letter of the word to be guessed

wrong = 0                    # number of wrong guesses player has made 

used = []                    #letters already guessed 


#The Main Loop 

print("Welcome to Hangman. Good luck!")

while wrong < MAX_WRONG and so_far != word:
    print(HANGMAN[wrong])
    print("\nYou've used the following letters:\n", used)
    print("\nSo far, the word is: \n", so_far)


#Getting the Player's Guess

    guess = input("Enter your guess: ")
    guess = guess.upper()

    while guess in used:
        print("You've already guessed the letter", guess)
        guess = input("Enter your guess: ")
        guess = guess.upper()
    
    used.append(guess)


#Checking the Guess

    if guess in word:
        print("\nYes!", guess, "is in the word!")
    
    #create new so_far to include the guess
    
        new = "" 
    
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new 

    else:
        print("\nSorry,", guess, "isn't in the word.")
        wrong += 1
    
    
#Ending the Game 

if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print("You've been hanged!")
else:
    print("\nYou guessed it!")
    
print("The word was", word)

input("\n\nPress Enter to exit")
    
    
    

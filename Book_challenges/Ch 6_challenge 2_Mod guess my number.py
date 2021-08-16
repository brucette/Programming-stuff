# Guess my Number game with limited number of guesses
# Modified to use the ask_number() function


def ask_number(question):
    """Ask for a number within a range."""
    import random 
    the_number = random.randint(1,100)
    guess = int(input(question))
    tries = 0
    while guess != the_number and tries != 10: 
        if guess > the_number:
            print("Lower..")
        else:
            print("Higher..")
        guess = int(input(question))
        tries += 1
    
    if tries == 10 and guess != the_number:
        print("You're out of luck - number of tries exceeded!")
    else:
        print("You guessed it! The number was", the_number)
        print("And it only took you", tries, "tries!")
        
        
    
print("\tWelcome to 'Guess my number'!")
print("\nI'm thinking of a number between 1 and 100")
print("Try to guess it in as few attempts as possible.\n")

ask_number("Take a guess: ")


    
    

            
      

    



import random 

print("\tWelcome to 'Guess my number'!")
print("\nI'm thinking of a number between 1 and 100")
print("Try to guess it in as few attempts as possible.\n")

the_number = random.randint(1,100)
guess = int(input("Take a guess: "))
tries = 1

while guess != the_number and tries != 10:
    if guess > the_number:
        print("Lower..")
    else:
        print("Higher..")
    guess = int(input("Take a guess: "))
    tries += 1

if tries == 10 and guess != the_number:
    print("You're out of luck - number of tries exceeded!")            
      
else:
    print("You guessed it! The number was", the_number)
    print("And it only took you", tries, "tries!")


     

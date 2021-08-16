import random 

print("Pick a number between 1 and 100")
print("Let me try to guess it in as few attempts as possible!")
input("\npress enter to start") 

guess = random.randint(1,100)
print("\nI guess", guess) 

answer = input("Am I correct? ")

while answer != "yes":
    question = input("Is it higher or lower? ")
    if question == "lower":
        guess = random.randint(1,guess)
        print("\nI guess", guess,)
        answer = input("am I correct? ")
    elif question == "higher":
        guess = random.randint(guess,100) 
        print("\nI guess", guess)
        answer = input("am I correct? ")
print("\n\nYESS, I got it!") 

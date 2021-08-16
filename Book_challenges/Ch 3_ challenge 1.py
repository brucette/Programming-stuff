#Fortune Cookie Program
#Displays five unique fortunes at random 

import random

print("Welcome to the fortune program!")
print("I sense your future to be:\n") 

fortune = random.randint(1, 5)

if fortune == 1:
    print("Only great things await you oh grandious one")
elif fortune == 2:
    print("Unfortunately things are looking pretty bleak as of now. Pull yourself up the bootstraps! ")
elif fortune == 3:
    print("You are going in the right direction, keep tredding along you beast.")
elif fortune == 4: 
    print("blah blah blah, who cares..?")
else: 
    print("Too far gone, can't be helped")
    
input("\nPress enter to exit the program")

    

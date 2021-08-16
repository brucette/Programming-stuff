#program picks a random word and the player has to guess the word 
#the computer tells the player how many letters are in the word
#then the player gets 5 chances to ask if a letter is in the word, the computer can only respond yes or no. 

import random 
import time


WORDS = ("book", "console", "mat", "plant", "puzzle", "guitar", "sun", "energy", "life")

word = random.choice(WORDS)
number_of_queries = 0 

print("I am thinking of a word")
time.sleep(1)
print(".")
time.sleep(1)
print("..")
time.sleep(1)
print("....")
time.sleep(1)
print("...it has", len(word), "letters")
print("You can query if a specific letter is in the word.") 
print("After 5 queries you have to guess the word.")

queried_letter = input("which letter would you like to query?: ")

while number_of_queries != 4:
    if queried_letter in word:
        print("yes")
    else:
        print("no")
    number_of_queries += 1 
    queried_letter = input("which letter would you like to query?: ")
    
guess = input("Take your guess: ")

if guess == word:
    print("Yes you guessed correct!")
else:
    print("I'm sorry, that's not the word I was thinking of :( ")
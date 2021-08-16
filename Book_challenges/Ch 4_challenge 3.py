# improve Word Jumble so that each word is paired with a hint 
# player will be able to see hint when stuck 
# add a scoring system that rewards players who guess a jumble without asking for the hint  

import random 

WORDS = ("python", "jumble", "easy", "difficult", "xylophone")

HINTS = ("a legless creature", "sale with various things", "such are sundays", "such are mondays", "type of instrument")

word = random.choice(WORDS)
correct = word

index = 0
for word in WORDS:
    if word == correct:
        break
    index += 1
    
jumble =" "

while word: 
    position = random.randrange(len(word)) 
    jumble += word[position]
    word = word[:position] + word[(position + 1):]
    
print(
"""
        Welcome to Word Jumble!
Unscramble the letters to make a word. 
(Press the enter key at the prompt to quit.)
\nWrite 'hint' when promted for a guess, if you are stuck and would like a hint.
""")
print("The jumble is:", jumble)

guess = input("\nYour guess: ")
while guess != correct: 
    print("Sorry, that's not it.")
    guess = input("Your guess: ")
     
    if guess == "hint":
        print(HINTS[index])
        guess = input("Your guess: ")
    
if guess == correct:
    print("Thats's it! You guessed it!\n")
  

print("Thanks for playing.")

input("\n\nPress the enter key to exit.")    
#program prints a list of words in random order, printing all words and not repeating any. 

import random 

words = ["OVERUSED","MUTABLE","CORNBREAD","INVISIBLE","JEALOUS","MOUNTAIN"]

word = random.choice(words)

while words:
    for word in words: 
        print(word)
        words.remove(word)
        
        
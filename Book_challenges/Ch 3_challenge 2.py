# Coin fliping program 
# Flips a coin 100 times then tells you the nuber of heads and tails 

import random 

number_of_flips = 100
amount_of_heads = 0
amount_of_tails = 0

while number_of_flips > 0:
    flip_coin = random.randint(1,2) 
    number_of_flips = number_of_flips - 1
    if flip_coin == 1:
        amount_of_heads += 1
    else:
        amount_of_tails += 1

    
print("you got a total of ",amount_of_heads, "heads and a total of ", amount_of_tails, "tails")
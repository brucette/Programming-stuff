# Character Creator program - player can spend a total of 30 points to spend on four attributes: Strength, Health, Wisdom and Dexterity

total_points = 30
 
print("Welcome!")
print("""
You have a pool of 30 points to spend on 4 attributes. 
You can also take out points from an attribute to put back into the pool.
""")

attributes = {"strength":0, "health":0, "wisdom": 0, "dexterity":0}

while True:
    selection = input("Select strength, health, wisdom or dexterity to spend OR take out points: ")
    if selection not in attributes:
        print("\nI'm sorry I don't recognise the selection")
        continue        # skips the rest and goes back to begining of loop
    
    amount = int(input("Enter positive or negative amount: "))
    
    current_value = attributes[selection]
    
    att_sum = 0
    for point in attributes.values():    # To get the total value of attributes
        att_sum += point
    
    total_spent = att_sum + amount  
    
    
    negative_number = False    
    if current_value + amount < 0:
        negative_number = True
    
    if total_spent > 30 or negative_number: 
        print("\nThe amount is out of the allowed range")
        print(attributes)
        print("Points remaining: ", total_points, "\n")
        
    else:
        total_points -= amount
        attributes[selection] = current_value + amount
        print("\n",attributes)
        print("\nPoints remaining: ", total_points, "\n")
        
        



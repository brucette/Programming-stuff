# allows user to enter a male name and produces their father's name. User can add, replace or delete father-son pairs.

pairs = {"Anton":"Jarno Rantanen", "Mateusz":"Leon Mojsiejuk", "Jaden":"Will Smith", 
"William":"Prince Charles", "Brooklyn":"David Beckham"}

print("""Welcome to 'Who's Your Daddy'. 
The program lets you know the father of the listed names. You can also edit the list.\n
Anton
Mateusz
Jaden
William
Brooklyn\n""")

while True: 
    choice = input("""What would you like to do?
    0) Look up a father
    1) Add a father-son pair
    2) Replace a father-son pair 
    3) Delete a father-son pair\n
    """)

    if choice == "0":
        look_up = input("Enter name of a male: ")
        if look_up in pairs:
            print("The father is:", pairs[look_up],"\n")
        else:
            print("\nThat name doesn't exist, try adding it!\n")
             
    if choice == "1":
        new_son = input("What is the name of the son?")
        if new_son not in pairs:
            new_father = input("And who is the father?")
            pairs[new_son] = new_father
            print("\n", new_son, "has been added\n")
        else:
            print("\nThat name already exists!\n")
            
    elif choice == "2":
        replaced_son = input("What is the name of the son?")
        if replaced_son in pairs:
            replaced_father = input("And who is the new father?")
            pairs[replaced_son] = replaced_father
            print("\n",replaced_son, "has been replaced\n")
        else:
            print("\nThat name doesn't exist, try adding it!\n")
            
    elif choice == "3":
        delete_son = input("What is the name of the son?")
        if delete_son in pairs:
            del pairs[delete_son]
            print("\n",delete_son, "has been deleted\n")
        else:
            print("\nI can't do that, the name doesn't exist!\n")
            
    
            
    
    


# allows user to enter a male name and produces their father's name. User can add, replace or delete father-son pairs. Improves previous version by allowing user to get name of grandfather when entering a name. Should still only use one dictionary of son-father pairs. 


pairs = {"Anton": {"father": "Jarno Rantanen", "grandfather": "Jussi Rantanen"}, "Mateusz": {"father": "Leon Mojsiejuk", "grandfather": "Andre Mojsiejuk"}, 
"Jaden": {"father": "Will Smith", "grandfather": "Willard Smith"}, "William": {"father": "Prince Charles", "grandfather": "Prince Philip"}, 
"Brooklyn": {"father": "David Beckham", "grandfather": "Ted Beckham"}}

sons = ["Anton", "Mateusz", "Jaden", "William", "Brooklyn"]

print("""Welcome to 'Who's Your Daddy'. 
The program lets you know the father or gradfather of the listed names. You can also edit the list.\n
""")

while True: 
    print(sons)
    choice = input("""What would you like to do? \n
    0) Look up a father
    1) Add a father-son pair
    2) Replace a father-son pair 
    3) Delete a father-son pair
    4) Get a grandfather\n
    """)
    
    
    if choice == "0":
        look_up = input("Enter name of a male: ")
        if look_up in pairs:
            print("The father is:", pairs[look_up]["father"],"\n")
        else:
            print("\nThat name doesn't exist, try adding it!\n")
             
    if choice == "1":
        new_son = input("What is the name of the son? ")
        if new_son not in pairs:
            new_father = input("And who is the father? ")
            new_grandfather = input("Who is the grandfather? ")
            pairs[new_son] = {"father": new_father, "grandfather": new_grandfather} 
            sons.append(new_son)
            print("\n", new_son, "has been added\n")
        else:
            print("\nThat name already exists!\n")
            
            
    elif choice == "2":
        replaced_son = input("What is the name of the son? ")
        if replaced_son in pairs:
            replaced_father = input("And who is the new father? ")
            replaced_grandfather = input("Who is the new grandfather? ")
            pairs[replaced_son] = {"father": replaced_father, "grandfather": replaced_grandfather}
            print("\n",replaced_son, "has been replaced\n")
        else:
            print("\nThat name doesn't exist, try adding it!\n")
            
            
    elif choice == "3":
        delete_son = input("What is the name of the son? ")
        if delete_son in pairs:
            del pairs[delete_son]
            sons.remove(delete_son)
            print("\n",delete_son, "has been deleted\n")
        else:
            print("\nI can't do that, the name doesn't exist!\n")
                
                
    elif choice == "4":
        male = input("Enter name of male: ")
        if male in pairs:
            print("The grandfather is:", pairs[male]["grandfather"],"\n")
        else:
            print("\nThat name doesn't exist, try adding it!\n")


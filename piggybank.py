balance = 0

while True:
    action = int(input("""\
        Please select an action.
        1) Make a deposit
        2) Withdraw money
        3) View balance
        4) Quit
        """))
    if action == 1:
        deposit = int(input("How much?: ")) 
        balance += deposit

    elif action == 2:
        withdraw = int(input("How much?: "))
        balance -= withdraw
    
    elif action == 3:
        print(balance)
        
    else:
        break
        



            
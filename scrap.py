text_file = open("read_it.txt")
print(text_file.readline(1))
print(text_file.readline(5))
text_file.close()


score_board = open("Score_board.txt") 
Computer = print(score_board.readline(25))
print(Computer)
Human = score_board.readline(34)
print(Human)
    
attributes = {"strength":0, "health":0, "wisdom": 0, "dexterity":0}

att_sum = 0

selection = "strength"

while selection in attributes:
    selection = input("Select strength, health, wisdom or dexterity to spend OR take out points: ")
    amount = int(input("Enter positive or negative amount: "))
    
    current_value = attributes[selection]
    print(current_value)
    
    for point in attributes.values():   
        att_sum += point
    print(att_sum)
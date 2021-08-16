#Gets a message from user and then prints it backwards

statement = input("enter something: ")
high = int(len(statement)-1)

for letter in range(high, -1, -1):
    print(statement[letter], end="" )
print("")

#OR 

statement = input("enter something: ")
high = int(len(statement))-1

for letter in statement:
    print(statement[high],end="")
    high -= 1
    
print("")
    
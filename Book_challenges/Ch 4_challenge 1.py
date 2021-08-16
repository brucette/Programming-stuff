# counting program 
# user enters the start and finish number and by how much to count

print("Welcome to the counting program!")

start_number = int(input("\nPlease enter the starting number: "))
end_number = int(input("And enter the ending number: "))
interval = int(input("By what incremental number do you want to count? Please enter: "))

for i in range(start_number, end_number, interval):
    print(i)


def give_me_five():
    five = 5
    return five
    
number = give_me_five()
print("Here's what I got from give_me_five():", number)



def ask_yes_no(question):
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response
    
answer = ask_yes_no("\nPlease will you sleep with me, y or n?")
print("Ok then,", answer,"!")



def bigger_than_five(number):
    
    return number > 5
    
num = int(input("specify a number"))

if bigger_than_five(num):
    # print(number)
    print("your number is to big")
print(num)
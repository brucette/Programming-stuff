import time
print("welcome to the bomb countdown")
seconds = int(input("arm the bomb by specifying the amount of seconds before boom:\n"))


while seconds != 0:
    print(seconds)
    seconds = seconds -1
    time.sleep(1)
    
print("boooom")

count = 0 
while True: 
    count += 1 
    if count > 10:
        break
    if count == 5:
 
        continue 
        
print(count)
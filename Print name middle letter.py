#get user to enter a name and then print the middle letter of the name 

name = input("enter name: ")
len_of_name = int(len(name))
mid_index = len_of_name // 2 
print(mid_index)
print(name[mid_index])


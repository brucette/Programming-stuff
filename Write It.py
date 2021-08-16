# Write It 
# Demonstrates writing to a text file 

print("Creating a text file with the write() method.")
text_file = open("write_it.txt", "w")
text_file.write("Line 1 \n")
text_file.write("This is line 2\n")
text_file.write("That would make this line 3\n")
text_file.close()

print("\nReading the newly created file.")
text_file = open("write_it.txt", "r")
print(text_file.read())
text_file.close()


print("Creating a text file with the writelines() method.")
text_file = open("write_it.txt", "w")
lines = ["Line 1\n", "This is line 2\n", "That would make this line 3\n"]
text_file.writelines(lines) 
text_file.close()

print("\nReading the newly created file.")
text_file = open("write_it.txt", "r")
print(text_file.read())
text_file.close()




import pickle 


the_list = ["biceps", "abs", "back", "booties", "quads", "hamstrings"]

the_file = open("pickled_words.dat", "wb")
pickle.dump(the_list, the_file)
the_file.close()

the_file = open("pickled_words.dat", "rb")
the_list = pickle.load(the_file)
print(the_list)



for word in the_list:
    length = len(word)
    print(length)





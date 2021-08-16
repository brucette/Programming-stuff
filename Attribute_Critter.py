
class Critter(object):
    def __init__(self, name):
        print("A new critter has been born!")
        self.name = name
        
    def talk(self):
        print("Hi, my name is", self.name, "\n")
        
    def __str__(self):        # a special method that represents the object as a string
        rep = "Critter object\n"
        rep += "name: " + self.name + "\n"
        return rep
                                                    
        
crit1 = Critter("Goofy")
crit1.talk()

crit2 = Critter("Loopy")
crit2.talk()

print(crit1)
print(crit2)







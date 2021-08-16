# demonstrates class attributes and static methods (apply to the whole class)
class Critter(object):
    total = 0 
    
    @staticmethod
    def status():
        print("The total number of critters is", Critter.total)
        
    def __init__(self, name):
        print("A new critter has been born!")
        self.name = name
        Critter.total += 1
        

print ("Accessing the class attribute Critter.total:", end=" ")
print(Critter.total)

print("\nCreating critters.")
crit1 = Critter("Bloopy")
crit2 = Critter("Scoopy")
crit3 = Critter("Doopy")                                                    
 
Critter.status()

print("\nAccessing the class attribute through an object:", end= " ")
print(crit1.total)









# demonstrates properties(an object w methods that allow indirect accesss to attributes ans often impose some sort of restriction)


class Critter(object):
        
    def __init__(self, name):
        print("A new critter has been born!")
        self.__name = name    
        
    @property
    def name(self):                     
        return self.__name
        
    @name.setter
    def name(self, new_name):                                       # method name has to be the same as in property
        if new_name == " ":
            print("Acritter's name can't be the empty string.")
        else:
            self.__name = new_name
            print("Name change successful.")
            
    def talk(self):
        print("\nHi, I'm", self.name)
        
        
#main
crit = Critter("Poochie")
crit.talk()                                     # accessess the property and indirectly calls the method that returns the private name

print("\nMy critter's name is:", end = " ")
print(crit.name)                                 # accessess the property from outside the Critter class and indirectly calls the method that returns the private name


print("\nAttempting to change my critter's name to Randolph...")
crit.name = "Randolph"

print("\nMy critter's name is:", end = " ")
print(crit.name)   
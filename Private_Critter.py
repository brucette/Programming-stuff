# demonstrates private attributes and methods
class Critter(object):
        
    def __init__(self, name, mood):
        print("A new critter has been born!")
        self.name = name    # public attribute
        self.__mood = mood  # private attribute

    def talk(self):
        print("\nI'm", self.name)
        print("Right now I feel", self.__mood, "\n")

    def __private_method(self):
        print("This is a private method.")
        
    def public_method(self):
        print("This is a public method.")
        self.__private_method()
        
        
crit = Critter("Poochie", "happy")
crit.talk()
crit.public_method()
import random 


class Farm:
    
    def __init__(self, name):
        self.name = name
        self.animals = []
    
    
    def create_critter(self, alist):
        for name in alist:
            crit = Critter(name)
            self.animals.append(crit)
         
         
    def __str__(self):
        farm_info = "Farm Object\n" + "name: " + self.name + "\nnumber of critters: " + str(len(self.animals))
        return farm_info
        
        
    def talk_summary(self):
        for animal in self.animals:
            animal.talk()
            
            
    def eat_summary(self):
        for animal in self.animals:
            animal.eat()
   
   
    def play_summary(self):
        for animal in self.animals:
            animal.play()
   
   
class Critter:
    
    def __init__(self, name):
        self.name = name
        self.hunger = random.randint(0,8)
        self.boredom = random.randint(0,8)
        
        
    def __pass_time(self):      # increases critters hunger and boredom levels 
        self.hunger += 1
        self.boredom += 1
    
    
    def talk(self):
        print("I'm", self.name, "and I feel", self.mood, "now.\n")
        self.__pass_time()
        
        
    def eat(self, food_amount = 4): 
        print("Brrupp. Thank you.")
        self.hunger -= food_amount
        if self.hunger < 0:
            self.hunger = 0 
        self.__pass_time()
        
        
    def play(self, play_time = 3):
        print("Wheee!")
        self.boredom -= play_time
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()
           
                
    def __str__(self):
        all_info = "Critter Object\n" + "name: " + self.name + "\nhunger: " + str(self.hunger) + "\nboredom: " +  str(self.boredom)
        return all_info
            
            
    @property
    def mood(self):         # calculates mood by adding hunger and boredom together 
        unhappiness = self.hunger + self.boredom 
        if unhappiness < 5:
            m = "happy"
        elif 5 <= unhappiness <= 10:
            m = "okay"
        elif 11 <= unhappiness <= 15:
            m = "frustrated"
        else:
            m = "mad"
        return m
    
def main():
    
    print("Welcome to your critter farm.") 
    
    names = input("Please give a list of names for your critters: \n")
    names = names.split()   # makes the entry into a list

    farm1 = Farm("Dangles")
    farm1.create_critter(names)

    print("""\nA new critter farm has been born!\n
    
    Time to interact with you critters!""")
    
    choice = None
    while choice != "0":
            
        choice = input("""
        What would you like to do?\n
        
        0 - Quit
        1 - Talk to your critters
        2 - Feed your critters
        3 - Play with your critters
        4 - View farm status
        5 - View critter status
        \n""")
            
        if choice == "0":
            print("Goodbye")
            
        elif choice == "1":
            farm1.talk_summary()
            
        elif choice == "2":
            farm1.eat_summary()

        elif choice == "3":
            farm1.play_summary()
            
        elif choice == "4":
            print(farm1,"\n")
            
        elif choice == "5":
            for animal in farm1.animals:
                print(animal,"\n")
            
        else:
            print("\nSorry, but", choice , "isn't a valid choice.")
            
            
main()
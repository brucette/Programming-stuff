# a virtual pet to care for 


class Critter(object):
        
    def __init__(self, name, hunger=0, boredom =0):
        self.name = name 
        self.hunger = hunger   
        self.boredom = boredom
        
    def __pass_time(self):      # increases critters hunger and boredom levels 
        self.hunger += 1
        self.boredom += 1 
    
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
        
    def talk(self): 
        print("I'm", self.name, "and I feel", self.mood, "now.\n")
        self.__pass_time()
        
    def eat(self):
        food_amount = int(input("How much food do you want to give? Choose between 1-4: "))
        while food_amount < 1 or food_amount > 4:
            food_amount = int(input("please enter valid amount: "))
        print("Brrupp. Thank you.")
        self.hunger -= food_amount
        if self.hunger < 0:
            self.hunger = 0 
        self.__pass_time()
        
    def play(self):
        play_time = int(input("How long do you want to play? Choose between 1-4 (15min increments): "))
        while play_time < 1 or play_time > 4:
            play_time = int(input("please enter valid choice: "))
        print("Wheee!")
        self.boredom -= play_time
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()
        
        
def main():                 # main part of the program is its own function 
    crit_name = input("What would you like to name you critter?: ")
    crit = Critter(crit_name)
    
    choice = None 
    while choice != "0":
        print \
        ("""  
        Critter Caretaker 
        
        0 - Quit
        1 - Listen to your critter
        2 - Feed your critter
        3 - Play with your critter
        """)
    
        choice = input("Choice: ")
        print()
               
    # exit
        if choice == "0":
            print("Good-bye")
        
    # listen to your critter
        elif choice == "1":
            crit.talk()
        
    # feed your critter
        elif choice == "2":
            crit.eat()
        
    #play with your critter
        elif choice == "3":
            crit.play()
    # some unknown choice
        else:
            print("\nSorry, but", choice , "isn't a valid choice.")
        
main()
("\n\nPress the enter key to exit.")
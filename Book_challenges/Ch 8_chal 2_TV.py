# a program that simulates a television 

class Gadget:
        
    def __init__(self):
        print("Welcome") 
          
          
    def channel(self):
                while True: 
                    valid_channel = False
                    valid_range = False
                    
                    try:
                        select_channel = int(input("Select a channel between 1-5: "))
                    except ValueError:
                        print("Selection is not a number")
                        continue                            # loop starts again
                    
                    valid_channel = True
                    
                    if select_channel in [1,2,3,4,5]:
                        valid_range = True
                        print("Channel selected: ", select_channel)
                    else:
                        print("Selection is out of range, there are currently 5 channels installed.")
                    
                    if valid_channel and valid_range:
                        break
                    
                    
    def volume(self, volume = 5):
        self.volume = volume 
        print("Volume currently at level", volume,"\n")
        
        while True:
            valid_volume = False
            
            try:
                set_volume = int(input("Select desired volume level between 1-10: "))
            except ValueError:
                print("Selection is not a number")
                continue                            # loop starts again
                
            valid_volume = True
            
            if valid_volume:
                break
                
        self.volume = set_volume
        print("\nVolume level set to", self.volume)
        
        
        
def main():
    television = Gadget()
    print("\n")
    
    choice = None 
    while choice != "0":
        print \
        ("""  
        Make a selection: 
        
        0 - Quit
        1 - Select channel
        2 - Set volume
        """)
    
        choice = input("Choice: ")
        
        
        if choice == "0":
            print("Good-bye")
            print("\n")
        
        elif choice == "1":
            television.channel()
            print("\n")
    
        elif choice == "2":
            television.volume()
            print("\n")
       
        else:
            print("\nSorry, but", choice , "isn't a valid choice.")
   
    
main()
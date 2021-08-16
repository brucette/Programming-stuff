#Car salesman program, user enters base price, additional prices added and total displayed

base_price = int(input("What is the price of the car? "))
tax = base_price * 0.10
print("The tax is ten percent of the base price,",(str((int(tax))))+".")
license = base_price * 0.20
print("The license is 20% of the base price,",(str((int(license))))+".")

dealer_prep = 2000
print("The dealer prep comes to",(str(dealer_prep))+".")
destination_charge = 2700
print("The destination charge comes to",(str(destination_charge))+".")

total = int(base_price + tax + license + dealer_prep + destination_charge)
print("\nThe Grand Total: ",total)

input("Press the enter key to exit.")
print("\a")

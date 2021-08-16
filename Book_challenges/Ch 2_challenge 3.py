#tipper program, displays price with 15 and 20 percent tip

total_bill = int(input("What is the total of the bill? "))
tip_15 = total_bill * 1.15
print("with a tip of 15 percent comes to a total of", tip_15)
tip_20 = total_bill * 1.20
print("with a tip of 20 percent comes to a total of", tip_20)
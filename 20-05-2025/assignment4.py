total_amount = input("enter your total purchase amount: ")
total_amount = int( total_amount)
if total_amount > 100:
    print("you get a discount of 10% ")
elif total_amount > 50:
    print("you get a discount of 5% ")
else:
    print("no discount")
    
print("final amount after discount")    
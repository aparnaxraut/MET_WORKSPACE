number1=int(input("enter the first number"))
number2=int(input("enter the first number"))
number3=int(input("enter the first number"))
number4=int(input("enter the first number"))
number5=int(input("enter the first number"))
order=list[number1,number2,number3,number4,number5]
print(order)
i=int(input("enter a random number"))

for item in order:
    if item == i:
        print("item found")
        break
    
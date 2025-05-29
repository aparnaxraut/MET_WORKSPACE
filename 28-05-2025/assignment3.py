count=0
while count<5:
    user=int(input("enter a number"))
    if user %2==0:
        print("even")
        break
    count+=1
else:
    print("all even numbers")
user1=input("enter a name")
user2=input("enter a name")
user3=input("enter a name")
user4=input("enter a name")
user5=input("enter a name")
user=list[user1,user2,user3,user4,user5]
print(user)
for i in user:
    if i in user:
        print("name exists")
        break
else:
    print("loop ended")
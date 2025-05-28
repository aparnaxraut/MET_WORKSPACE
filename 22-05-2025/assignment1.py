user=int(input("enter your first number"))
user1=int(input("enter your second number"))
user3=input("enter an operation")
def add (a,b):
    print(a+b)
def subtract (a,b):
    print(a-b)
def multiply():
    print(user1*user)
def devide():
    print(user1/user)
if user3=="+":
    add(user,user1)
elif user3=="-":
    subtract()
elif user3=="*":
    multiply()
elif user3=="/":
    devide()

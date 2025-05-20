users={ "username":"aparna",
       "password":"hey python"
}
username = input("enter your username ")
password = input("enter your password ")
if username == users["username"] and password == users["password"]:
    print(" welcome")
else:
    print("invalid username or password")
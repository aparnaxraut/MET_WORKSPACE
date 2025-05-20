secret_number=input("give a secret number")
secret_number=int(secret_number)
number=input(" give a number")
number=int(number)
if secret_number == number:
    print(" your guess is exactly right")
elif secret_number > number:
    print("your secret number is higher than the guessed number ")
else:
    print("your secret number is lower than the guessed number ")
    
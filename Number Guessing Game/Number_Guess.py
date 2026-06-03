import random
Secret_number = random.randint(1,100)
print("Starting Guessing Game")
attempts = 0

while True:
    guess = int(input("Enter Your Guess : "))
    attempts+=1

    if guess < Secret_number:
        print("Small")
    elif guess > Secret_number:
        print("High")
    else:
        print("Correct")
        print("Total attempts taken : ",attempts)
        break


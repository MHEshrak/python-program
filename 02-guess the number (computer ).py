import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Enter a number between {1} to {x}: "))
        if guess < random_number:
            print(f"{guess} is to low: ")
        elif guess > random_number:
            print(f"{guess} is to high")
    print(f"{guess} is Correct!!!")


guess(100)
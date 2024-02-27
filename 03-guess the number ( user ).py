import random
import time


def computer_guess(x):
    global computer_number
    low = 1
    high = x
    user_hint = 0

    print(f"guess a number between {low}-{high}")
    time.sleep(3)

    while user_hint != "c":
        if low != high:
            computer_number = random.randint(low, high)
        else:
            computer_number = low  # this could be high because high = low
        user_hint = input(f"Is {computer_number} high (h), low (l) or correct (c): ").lower()
        if user_hint == "h":
            high = computer_number - 1
        elif user_hint == "l":
            low = computer_number + 1
    print(f"Yay Computer guess the number {computer_number}")


computer_guess(1000)

import random


def guess(x):
    random_number = random.randint(1, x)
    # print(random_number)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))

        if guess < random_number:
            print("Sorry guess again. Too low")
        elif guess > random_number:
            print("Sorry guess again. Too high")

    print(f"Yay congrats! You guessed the number {random_number} right")


# guess(10)


def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        guess = random.randint(low, high)

        feedback = input(f"Is {guess} too high (H), too low (L) or correct (C)?? ").lower()

        if feedback == "h":
            high = guess - 1
        if feedback == "l":
            low = guess + 1

    print("You guessed the number right!")


computer_guess(10)

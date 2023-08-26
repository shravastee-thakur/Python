import random
print(" 0 for rock, 1 for paper, 2 for scissor")
user_choice = int(input("Enter your choice: "))

if user_choice >= 3 or user_choice < 0:
    print("Invalid input")
else:

    computer_choice = random.randint(0, 2)

    print(f"Computer chose: {computer_choice}")

    if computer_choice == user_choice:
        print("Its a draw.")

    elif computer_choice == 0 and user_choice == 2:
        print("You lose.")

    elif computer_choice == 2 and user_choice == 0:
        print("You win.")

    elif computer_choice > user_choice:
        print("You lose.")

    elif computer_choice < user_choice:
        print("You win.")

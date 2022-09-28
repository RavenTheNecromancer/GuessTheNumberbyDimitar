import random

print("Difficulties:\neasy (Numbers between 1-10)\nnormal (Numbers between 1-100)\nhard (Numbers between 1-1000)")
player_choice = input("Select difficulty: ")

if player_choice == "easy":
    computer_gen_number = random.randint(1,10)
elif player_choice == "normal":
    computer_gen_number = random.randint(1, 100)
elif player_choice == "hard":
    computer_gen_number = random.randint(1, 1000)
else :
    raise SystemExit("Invalid Input. Try again with one of the valid options!")


while True:
    player_guess = input("Make your guess: ")

    if not player_guess.isdigit():
        print("Invalid input! Try again.")
        continue

    player_number = int(player_guess)
    if player_number == computer_gen_number:
        print("Correct guess! YOU WIN!")
        break
    elif player_number > computer_gen_number:
        print("Too high!")
    else:
        print("Too low!")

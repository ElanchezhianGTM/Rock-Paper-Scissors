import random
import os

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

print("Welcome to Rock, Paper, Scissors game")

continue_game = True
games_played = 0
user_won = 0

while continue_game:
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    if user_choice >= 3 or user_choice < 0:
        print("Enter values between 0, 1 & 2 to play the Game")
        continue_option = input("Do you wanna restart again?: 'Y' or 'N'\n").lower()
        if continue_option == 'y':
            continue_game = True
        else:
            print("Bye, Have a Nice Day!")
            os.system('cls' if os.name == "nt" else 'clear')
            break
    else:
        print(f"You chose:")
        print(game_images[user_choice])
        computer_choice = random.randint(0, 2)
        print(f"Computer chose: ")
        print(game_images[computer_choice])
        if user_choice == computer_choice:
            print("It's a Draw")
        elif user_choice == 0 and computer_choice == 2:
            print("You Win!")
            user_won += 1
        elif user_choice == 2 and computer_choice == 0:
            print("You Lose!")
        elif user_choice > computer_choice:
            print("You Win!")
            user_won += 1
        elif computer_choice > user_choice:
            print("You Lose!")
        else:
            print("You Lose!")

        games_played += 1

        c = input("Do you want to restart and play again, Type 'Y' to restart or Type 'N' to exit game: ").lower()
        if c == "y":
            continue_game = True
        else:
            continue_game = False
            print(f"You have won {user_won} times out of {games_played}")
            print("Bye, Have a Nice Day!")
            os.system('cls' if os.name == "nt" else 'clear')
            break

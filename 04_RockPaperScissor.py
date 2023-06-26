import random
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

game_image = [rock, paper, scissors]
is_again = True
while is_again:
    user_choice = int(input(
        "what do you choose? Type 0 for rock, Type 1 for paper, Type 2 for scissors."))

    if user_choice <= 2 or user_choice > -1:
        print(game_image[user_choice])
        computer_choice = random.randint(0, 2)
        print("Computer choice:")
        print(game_image[computer_choice])

        if user_choice == 0 and computer_choice == 2:
            print("You Win!")
        elif computer_choice == 0 and user_choice == 2:
            print("You lose!")
        elif computer_choice > user_choice:
            print("You Win!")
        elif user_choice > computer_choice:
            print("You lose!")
        elif computer_choice == user_choice:
            print("It's a Draw")
    else:
        print("You typed an invaild number, you lose.")
    if input("Play again!") == "n":
      is_again = False

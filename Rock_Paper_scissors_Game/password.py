# import random module
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

# add rock,paper,scissors into list
game_image = [rock,paper,scissors]

# get input from user
# convert it into int because when user enter input its string
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
print(game_image[user_choice])

# computer pick random number
computer_choice = random.randint(0, 2)
print("Computer Choose")
print(game_image[computer_choice])
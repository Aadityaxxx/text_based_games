import random

pc_choices = ['rock', 'paper', 'scissor']

def no_to_opt(num):
    if num == 1:
        return 'rock'
    elif num == 2:
        return 'paper'
    elif num == 3:
        return 'scissor'
    else:
        print("Wrong no. input.")


def start_game():
    choose = int(input("Rock, Paper, Scissors[1/2/3]:"))
    pc_choose = random.choice(pc_choices)
    h_choose = no_to_opt(choose)

    if h_choose == pc_choose:
        print('****************************************')
        print("You:", h_choose)
        print("Computer:", pc_choose)
        print('****************************************')
        print("Its Tie.")

    elif h_choose == 'rock' and pc_choose == 'paper':
        print('****************************************')
        print("You:", h_choose)
        print("Computer:", pc_choose)
        print('****************************************')
        print("You lose...")
        print('----------------------------------------')

    elif h_choose == 'rock' and pc_choose == 'scissor':
        print('****************************************')
        print("You:", h_choose)
        print("Computer:", pc_choose)
        print('****************************************')
        print("You won!")
        print('----------------------------------------')

    elif h_choose == 'paper' and pc_choose == 'scissor':
        print('****************************************')
        print("You:", h_choose)
        print("Computer:", pc_choose)
        print('****************************************')
        print("You lose...")
        print('----------------------------------------')

    elif h_choose == 'paper' and pc_choose == 'rock':
        print('****************************************')
        print("You:", h_choose)
        print("Computer:", pc_choose)
        print('****************************************')
        print("You won!")
        print('----------------------------------------')

    elif h_choose == 'scissor' and pc_choose == 'rock':
        print('****************************************')
        print("You:", h_choose)
        print("Computer:", pc_choose)
        print('****************************************')
        print("You lose...")
        print('----------------------------------------')

    elif h_choose == 'scissor' and pc_choose == 'paper':
        print('****************************************')
        print("You:", h_choose)
        print("Computer:", pc_choose)
        print('****************************************')
        print("You won!")
        print('----------------------------------------')

    else:
        print("Something went wrong.")


while True:
    game_input = input("Do you want to play game[y/n]:")
    if game_input == "y" or game_input == "Y":
        start_game()

    elif game_input == "n" or game_input == "N":
        break

    else:
        print("Invalid input.")

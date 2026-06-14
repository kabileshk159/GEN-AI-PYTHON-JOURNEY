import random

    

def win():
    player_choice= str((input('enter a choice(rock,paper,scissors):')))
    options=['rock', 'paper', 'scissors']
    computer_choice= random.choice(options)
    print('you chose',player_choice,'computer chose',computer_choice)
  
    if player_choice == computer_choice:
        print('its a tie')
    elif player_choice== 'rock' and computer_choice== 'scissors':
        print('rock smashes scissors, you win')
    elif player_choice== 'paper' and computer_choice== 'rock':
         print('paper wraps rock, you win')
    elif  player_choice== 'paper' and computer_choice== 'scissors':
        print('scissors cuts paper, you lose')
    elif player_choice== 'scissors' and computer_choice== 'paper':
        print('scissors cuts paper, you win')
    else:
        print('you lose')

    
win()

           

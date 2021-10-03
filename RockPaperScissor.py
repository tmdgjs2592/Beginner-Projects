import random

def is_winner(player, opponent):
    if (player=='r' and opponent =='s') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

def play():
    while True:
        user = input("Rock (r), Paper(p), Scissor(s), Which one would you like to choose?: ").lower()
        computer = random.choice(['r', 'p', 's'])
        if user == computer:
            print('It\'s a tie')
        elif is_winner(user, computer):
            print(f'You won, the computer picked {computer}')
        else:
            print(f'You lost, the computer picked {computer}')
        
        if user == 'q':
            break

play()


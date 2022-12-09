import random

candy_count = int(input('Enter candy count = '))
step_count = int(input('Enter step count = '))

def game_two_players(candy_count:int,step_count:int):
    player_number=1
    while candy_count!=0:
        step_player = int(input(f'Player {player_number} takes candy: '))
        if candy_count-step_player<0 or step_player>step_count:
            print('You cant take so many!')
        else:
            candy_count=candy_count-step_player
            print(f'Player {player_number} takes {step_player} candy and {candy_count} left ')
            if candy_count==0:
                print(f'Player {player_number} WIN ')
            if player_number ==1:
                player_number=2
            else:
                player_number=1
        

#game_two_players(candy_count,step_count)

def game_one_players(candy_count:int,step_count:int):

    player_who='Player'
    while candy_count!=0:
        if player_who =='Player':
            step_player = int(input(f'{player_who} takes candy: '))
        else:         
            step_player = random.randint(1, min(step_count,candy_count))
        if candy_count-step_player<0 or step_player>step_count:
            print('You cant take so many!')
        else:
            candy_count=candy_count-step_player
            print(f'{player_who} takes {step_player} candy and {candy_count} left ')
            if candy_count==0:
                print(f'{player_who} WIN ')
            if player_who =='Player':
                player_who='Bot'
            else:
                player_who='Player'

game_one_players(candy_count,step_count)

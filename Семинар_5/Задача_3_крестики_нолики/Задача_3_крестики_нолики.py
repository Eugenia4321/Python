
game_map=['1','2','3','4','5','6','7','8','9']

def print_game_map(game_map):
    i=0
    for _ in range(3):
         print(f'| {game_map[i]} | {game_map[i+1]} | {game_map[i+2]}|')
         print(f'____________')
         i+=3    
       
print_game_map(game_map)

#def game(game_map):
#    player_number = 1
#    win_chek=True 
#    while win_chek:
#        step = int(input(f'\nPlayer {player_number} do step : \n'))
#        if game_map[step-1] == '0' or game_map[step-1] == 'X':
#            print('Error\n')
#        else:
#            if player_number==1:
#                game_map[step-1] = 'X'
#                player_number=2
               
#            else:
#                game_map[step-1] = '0'
#                player_number=1
#        print_game_map(game_map)
#        win_chek=win_chek_function(game_map)
#    if player_number == 1:
#        print(f'Player 2 WIN')
#    else:
#        print(f'Player 1 WIN')
def game(game_map):
    player_number = 1
    win_chek=True 
    for i in range(0,9):
        step = int(input(f'\nPlayer {player_number} do step : \n'))
        if game_map[step-1] == '0' or game_map[step-1] == 'X':
            print('Error\n')
        else:
            if player_number==1:
                game_map[step-1] = 'X'
                player_number=2               
            else:
                game_map[step-1] = '0'
                player_number=1
        print_game_map(game_map)
        if not win_chek_function(game_map):
            return player_number
    return 0




def win_chek_function(game_map):
    if game_map[0]==game_map[1]==game_map[2]:
        return False 
    if game_map[3]==game_map[4]==game_map[5]:
        return False
    if game_map[6]==game_map[7]==game_map[8]:
        return False 
    if game_map[0]==game_map[3]==game_map[2]:
        return False 
    if game_map[1]==game_map[4]==game_map[7]:
        return False
    if game_map[2]==game_map[5]==game_map[8]:
        return False 
    if game_map[0]==game_map[4]==game_map[8]:
        return False 
    if game_map[2]==game_map[4]==game_map[6]:
        return False 
    else:
        return True

winner = game(game_map)
if winner == 1:
    print(f'Player 2 WIN')
if winner == 2:
    print(f'Player 1 WIN')
if winner == 0:
    print(f'no winner ')
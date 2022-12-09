
game_map=['1','2','3','4','5','6','7','8','9']

def print_game_map(game_map:list):
    """ Функция принимает список со значением полей и  печатает рисунок крестиков - ноликов
    """
    i=0
    for _ in range(3):
         print(f'| {game_map[i]} | {game_map[i+1]} | {game_map[i+2]}|')
         print(f'____________')
         i+=3    
       
print_game_map(game_map)

def game(game_map:list):
    """ Игра в крестики нолики, принимает поле и возвращает номер проигравшего игрока или 0 если ничья
    Arguments:
             (list)game_map            
        Return:
             (int)player_number
    """
    player_number = 1
  
    for i in range(0,9): 
        step = input_step(game_map,player_number)          
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

def input_step(game_map,player_number):
    """ Проверка на ввод шага - от 1 до 9 в незанятую ячейку, возвращает допустимый шаг
    Arguments:
             (list)game_map 
             (int)player_number
        Return:
             (int)step
    """    
    while True:
        step = int(input(f'\nPlayer {player_number} do step : \n'))
        if 0<step<9:
            if  game_map[step-1] != '0' and game_map[step-1] != 'X' :
                return step
            else:
                print('error')
        else:
            print('error')
    
def win_chek_function(game_map:list):
    """Проверка на победителя, возвращает False если игрок победил и игра закончена
        
    """
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
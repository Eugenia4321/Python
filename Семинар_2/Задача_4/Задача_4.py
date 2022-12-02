#4 - ѕо кругу сто€т n человек. ¬едущий посчитал m человек по кругу, начина€ с первого. 
#ѕри этом каждый из тех, кто участвовал в этом счете, получил по одной монете, остальные получили по две монеты.
#ƒалее человек, на котором остановилс€ счет, отдает все свои монеты следующему по счету человеку, а сам выбывает из круга. 
#ѕроцесс продолжаетс€ с места остановки аналогичным образом до последнего человека в круге. —оставьте алгоритм, который проводит эту игру. 
#≈сли хотите делать паузы, то импортируйте библиотеку time и используйте оттуда функцию sleep.
#ќпределите номер этого человека и количество монет, которые оказались у него в конце игры.


from operator import countOf
from re import A


people =int(input('people = '))
count =int(input('count = '))

def Create_list_people(people):
    list_people = list(range(0, people ))
    return list_people

def Create_list_coins(people):
    list_coins = list(range(0, people ))    
    for i in range(people):
        list_coins[i]=0
    return list_coins

def plus_one_coin(list_people,list_coins):
    index_coins=0
    for ii in range(count):   
        if list_coins[list_people[index_coins]]==-1:
              index_coins+=1
        else:    
              if index_coins==len(list_people)-1:
                  list_coins[list_people[index_coins]]+=1
                  index_coins=0
              else:
                  list_coins[list_people[index_coins]]+=1
                  index_coins+=1

def Plus_two_coins(count,list_people,list_coins,stop_step):
    if count <len(list_people):
        for i in range(stop_step+1,len(list_people)):      
            list_coins[list_people[i]]+=2


def Delete_player_with_coins_transfer(list_people,list_coins,stop_step):
    index_for_summ=stop_step+1
    if list_coins[index_for_summ]==-1:
        if index_for_summ==len(list_people)-1:
                list_coins[stop_step+1]=list_coins[stop_step+1]+list_coins[stop_step]
                index_for_summ+=0
        index_for_summ+=1
    list_coins[list_people[stop_step+1]]=list_coins[list_people[stop_step+1]]+list_coins[list_people[stop_step]]
    list_coins[list_people[stop_step]]=-1
    delete_player = list_people[stop_step]
    list_people.remove(list_people[stop_step])
    return delete_player

def Changing_player_positions(stop_step,list_people):
    for i in range(0,stop_step):
             list_people.append(list_people[0])
             list_people.remove(list_people[0])

def Print_step_with_result(list_people,list_coins,delete_player):
    list_people_sort = list_people[:]
    list_people_sort.sort()
    print(f'Player {delete_player+1} leaves the game\n')
    for i in range(len(list_people)):
        print(f'Player {list_people_sort[i]+1} with {list_coins[list_people_sort[i]]} coins')
    input('\n\npress enter to continue\n\n')

def Game(people,count):
    list_people = Create_list_people(people)
    list_coins = Create_list_coins(people)
    for i in range(people - 1):   
         stop_step = count%len(list_people)-1
         Plus_two_coins(count,list_people,list_coins,stop_step)
         plus_one_coin(list_people,list_coins)
         delete_player = Delete_player_with_coins_transfer(list_people,list_coins,stop_step)
         Changing_player_positions(stop_step,list_people)
         Print_step_with_result(list_people,list_coins,delete_player)
    print('winner is ', list_people[0]+1,' player with ',list_coins[list_people[0]],' coins')

Game(people,count)

exit()
people =13# int(input('people = '))
count =4# int(input('count = '))
list_people = list(range(0, people ))
list_coins = list(range(0, people ))
#print('list_coins',list_coins)
for i in range(people):
    list_coins[i]=0
#print('list_coins',list_coins)
for i in range(people - 1):
   # print('Step',i)
    stop_step = count%len(list_people)-1        #остаток если каунт больше длины
   # print('a',a)
    index_coins=0
    if count <len(list_people):
        for cc in range(stop_step+1,len(list_people)):
       # for cc in list_people[a+1:]:
            list_coins[list_people[cc]]+=2
    for ii in range(count):   
        if list_coins[list_people[index_coins]]==-1:
              index_coins+=1
        else:    
              if index_coins==len(list_people)-1:
                  list_coins[list_people[index_coins]]+=1
                  index_coins=0
              else:
                  list_coins[list_people[index_coins]]+=1
                  index_coins+=1
    index_for_summ=stop_step+1
    if list_coins[index_for_summ]==-1:
        if index_for_summ==len(list_people)-1:
            list_coins[stop_step+1]=list_coins[stop_step+1]+list_coins[stop_step]
            index_for_summ+=0
        index_for_summ+=1
    list_coins[list_people[stop_step+1]]=list_coins[list_people[stop_step+1]]+list_coins[list_people[stop_step]]
    list_coins[list_people[stop_step]]=-1
    list_people.remove(list_people[stop_step])
    
   # print('spisok',list_people)
   # print('coins',list_coins)
    for y in range(0,stop_step):
        list_people.append(list_people[0])
        list_people.remove(list_people[0])
      #  print('spisok1',list_people)
    
print('winner is ', list_people[0]+1,' player with ',list_coins[list_people[0]],' coins')
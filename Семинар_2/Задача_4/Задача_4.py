#4 - По кругу стоят n человек. Ведущий посчитал m человек по кругу, начиная с первого. 
#При этом каждый из тех, кто участвовал в этом счете, получил по одной монете, остальные получили по две монеты.
#Далее человек, на котором остановился счет, отдает все свои монеты следующему по счету человеку, а сам выбывает из круга. 
#Процесс продолжается с места остановки аналогичным образом до последнего человека в круге. Составьте алгоритм, который проводит эту игру. 
#Если хотите делать паузы, то импортируйте библиотеку time и используйте оттуда функцию sleep.
#Определите номер этого человека и количество монет, которые оказались у него в конце игры.


from operator import countOf
from re import A


people = int(input('people = '))
count = int(input('count = '))
list_people = list(range(0, people ))
list_coins = list(range(0, people ))
#print('list_coins',list_coins)
for i in range(people):
    list_coins[i]=0
#print('list_coins',list_coins)
for i in range(people - 1):
   # print('Step',i)
    a = count%len(list_people)-1
   # print('a',a)
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
    index_for_summ=a+1
    if list_coins[index_for_summ]==-1:
        if index_for_summ==len(list_people)-1:
            list_coins[a+1]=list_coins[a+1]+list_coins[a]
            index_for_summ+=0
        index_for_summ+=1
    list_coins[list_people[a+1]]=list_coins[list_people[a+1]]+list_coins[list_people[a]]
    list_coins[list_people[a]]=-1
    list_people.remove(list_people[a])
    
   # print('spisok',list_people)
   # print('coins',list_coins)
    for y in range(0,a):
        list_people.append(list_people[0])
        list_people.remove(list_people[0])
      #  print('spisok1',list_people)
    
print('winner is ', list_people[0]+1,' player with ',list_coins[list_people[0]],' coins')
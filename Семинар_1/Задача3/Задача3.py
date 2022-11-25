#3- Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

#Пример:

#x=34; y=-30 -> 4
#x=2; y=4-> 1
#x=-34; y=-30 -> 3 

def Check_quarter(x,y):
    if x>0 and y>0:
        return 1
    if x>0 and y<0:
        return 4
    if x<0 and y>0:
        return 2
    if x<0 and y<0:
        return 3

x = float(input('Enter x = '))
y = float(input('Enter y = '))
if x==0 or y ==0:
    print('Error')
else:
    print(Check_quarter(x,y))
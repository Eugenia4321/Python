#5- Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

#Пример:

#A (3,6); B (2,1) -> 5.09
#A (7,-5); B (1,-1) -> 7.21


import math


def Find_distance(xa,ya,xb,yb):
    distance = math.sqrt(((xb-xa)**2+(yb-ya)**2))
    return round(distance,2)

print('Enter A coordinates')
xa = int(input('Xa = '))
ya = int(input('Ya = '))

print('Enter B coordinates')
xb = int(input('Xb = '))
yb = int(input('Yb = '))

print(f'Distance beetwen A({xa}, {ya}) and B({xb}, {yb}) is {Find_distance(xa,ya,xb,yb)}')
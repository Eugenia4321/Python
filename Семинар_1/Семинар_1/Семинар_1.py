import math
#1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.

#*Примеры:*

#- 5, 25 -> да
#- 4, 16 -> да
#- 25, 5 -> да
#- 8,9 -> нет
#2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

#Примеры:

#- 1, 4, 8, 7, 5 -> 8
#- 78, 55, 36, 90, 2 -> 90
#3- Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

#*Примеры:*

#- 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5
#4-Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.

#*Примеры:*

#- 6,78 -> 7
#- 5 -> нет
#- 0,34 -> 3

def print_numbers():
    n=abs(int(input("enter numer = ")))
    for i in range(-n,n+1):
        print(i,end=' ')

def Sqr_number():
    first_number = int(input('a =  '))
    second_number = int(input('b = '))
    if first_number == second_number**2 or second_number == first_number**2:
        print('yes')
    else:
        print("no")

def Max_number():
    collection1=[]
    for i in range(5):
        collection1.append(int(input('enter number = ')))

    max_number = collection1[0]

    for i in range(1,5):
        if max_number<collection1[i]:
            max_number = collection1[i]

    print(max_number)

def first_number():
    a = float(input('enter number'))
    a = a *10
    a = int(a%10)
    print(a)

Sqr_number()
Max_number()
print_numbers()
first_number()

#numbers = input('введите через пробел 5 чисел: ')
#numbers = numbers.split(' ')
#print (numbers)
#maximum = int (numbers[0])
#for i in numbers:
#    i= int (i)
#    if maximum < i:
#        maximum = i
#print (maximum)
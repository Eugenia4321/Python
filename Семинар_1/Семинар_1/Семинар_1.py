import math
#1. �������� ���������, ������� ��������� �� ���� ��� ����� � ���������, �������� �� ���� ����� ��������� �������.

#*�������:*

#- 5, 25 -> ��
#- 4, 16 -> ��
#- 25, 5 -> ��
#- 8,9 -> ���
#2. �������� ���������, ������� �� ���� ��������� 5 ����� � ������� ������������ �� ���.

#�������:

#- 1, 4, 8, 7, 5 -> 8
#- 78, 55, 36, 90, 2 -> 90
#3- �������� ���������, ������� ����� �� ���� ��������� ����� N � �������� ����� �� -N �� N

#*�������:*

#- 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5
#4-�������� ���������, ������� ����� ��������� �� ���� ����� � ���������� ������ ����� ������� ����� �����.

#*�������:*

#- 6,78 -> 7
#- 5 -> ���
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

#numbers = input('������� ����� ������ 5 �����: ')
#numbers = numbers.split(' ')
#print (numbers)
#maximum = int (numbers[0])
#for i in numbers:
#    i= int (i)
#    if maximum < i:
#        maximum = i
#print (maximum)
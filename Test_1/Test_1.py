
from msilib.schema import BBControl
from pickle import TRUE
#from socket import AF_AAL5


q = None       #������������ ����������
b=0            # \n ����� ������
a=2.3          # \' ������ �������
               # "''" ������ �������   
               # int float boolean str list

#������������ �����
print(a,'-',b,'-')
print('{1}-{0}-'.format(a,b))
print('{}-{}-'.format(a,b))
print(f'{a} - {b} -')

print(type(a))  #����� ����
s = "'qwerty'"

#���������� ����������

f= False 

#������

list = [1,2,3]
list1= ['1','1','1']

#���� ������
b1 = input()
#�����
a1=int(input())
a2=float(input())

#��������
# +-*/
# // ������������� ������� 
#% ������� �� �������
#** ���������� � �������

c = round(a*b,3)    #����������� �� 3 ������, ��� 3 ����� �� ������ �����

a+=5

#���������� ��������

#> >= < <= == !=
#not and or 
#is, is not, in, not in

f11=[1,2,3,4]
print(f11)
print(not 2 in f11)

#������������� ������� a<b<c ��� a<b<v>c

# 0 ����, 1 ������

is_odd = f11[0]%2==0 # is_odd = not f11[0]%2

#����� ���������

aa= int(input('a= '))
bb= int(input('b= '))
if aa>bb: 
    print(aa)
else:
    print(bb)

if aa==1:
    print(aa)
elif aa==2:
    print(aa)
elif aa==2:
    print(aa)
else:
    print(aa)

#�����
aaa=3
while b<=aaa: 
    b+=1
else:
    print(b)


# for

for i in 1,2,3,4,5:
    print(i**2)

list1=[1,2,3,4,5]
for i in list1:
    print(i**2)

r = range(10)
for i in r:
    print(i**2)

for i in range(10):
    print(i**2)

for i in range(1,10,2):     # [1,10) � ����� 2
    print(i**2)

for i in 'qwerty':
    print(i)


text = '����� ��� ���� ������ ����������� �����'
print(len(text)) # 39
print('���' in text) # True
print(text.isdigit()) # False
print(text.islower()) # True
print(text.replace('���','�٨')) #
for c in text:
    print(c)

text = '����� ��� ���� ������ ����������� �����'
print(text[0]) # c
print(text[1]) # �
print(text[len(text)-1]) # �
print(text[-5]) # �
print(text[:]) # print(text)
print(text[:2]) # ��
print(text[len(text)-2:]) # ��
print(text[2:9]) # ��� ���
print(text[6:-18]) # ��� ���� ������
print(text[0:len(text):6]) # �������
print(text[::6]) # �������
text = text[2:9] + text[-5] + text[:2] # ...

numbers = [1, 2, 3, 4, 5]
print(numbers) # [1, 2, 3, 4, 5]
numbers = list(range(1, 6))
print(numbers) # [1, 2, 3, 4, 5]
numbers[0] = 10
print(numbers) # [10, 2, 3, 4, 5]
for i in numbers:
    i *= 2
    print(i) # [20, 4, 6, 8, 10]
print(numbers) # [10, 2, 3, 4, 5]

colors = ['red', 'green', 'blue']
for e in colors:
    print(e) # red green blue
for e in colors:
    print(e*2) # redred greengreen blueblue
colors.append('gray') # �������� � �����
print(colors == ['red', 'green', 'blue', 'gray']) # True
colors.remove('red') #del colors[0] # ������� �������

def function_name(x):
    return x**2
# body line 1
# . . .
# body line n
 # optional return

def f(x):
    if x == 1:
        return '�����'
    elif x == 2.3:
        return 23
    else:
        return

print(f(1)) # �����
print(f(2.3)) # 23
print(f(28)) # None
print(type(f(1))) # str
print(type(f(2.3))) # int
print(type(f(28))) # NoneType
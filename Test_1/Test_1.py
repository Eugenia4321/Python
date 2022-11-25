
from msilib.schema import BBControl
from pickle import TRUE
#from socket import AF_AAL5


q = None       #необъ€ленна€ переменна€
b=0            # \n нова€ строка
a=2.3          # \' печать кавычки
               # "''" печать кавычек   
               # int float boolean str list

#интерпол€ци€ строк
print(a,'-',b,'-')
print('{1}-{0}-'.format(a,b))
print('{}-{}-'.format(a,b))
print(f'{a} - {b} -')

print(type(a))  #вывод типа
s = "'qwerty'"

#логическа€ переменна€

f= False 

#массив

list = [1,2,3]
list1= ['1','1','1']

#ввод данных
b1 = input()
#число
a1=int(input())
a2=float(input())

#операции
# +-*/
# // целочисленное деление 
#% остаток от делени€
#** возведение в степень

c = round(a*b,3)    #окгругление до 3 знаков, без 3 будет до целого числа

a+=5

#логические операции

#> >= < <= == !=
#not and or 
#is, is not, in, not in

f11=[1,2,3,4]
print(f11)
print(not 2 in f11)

#множественные операци a<b<c или a<b<v>c

# 0 ложь, 1 истина

is_odd = f11[0]%2==0 # is_odd = not f11[0]%2

#циклы ветвлени€

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

#циклы
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

for i in range(1,10,2):     # [1,10) с шагом 2
    print(i**2)

for i in 'qwerty':
    print(i)


text = 'съешь ещЄ этих м€гких французских булок'
print(len(text)) # 39
print('ещЄ' in text) # True
print(text.isdigit()) # False
print(text.islower()) # True
print(text.replace('ещЄ','≈ў®')) #
for c in text:
    print(c)

text = 'съешь ещЄ этих м€гких французских булок'
print(text[0]) # c
print(text[1]) # ъ
print(text[len(text)-1]) # к
print(text[-5]) # б
print(text[:]) # print(text)
print(text[:2]) # съ
print(text[len(text)-2:]) # ок
print(text[2:9]) # ешь ещЄ
print(text[6:-18]) # ещЄ этих м€гких
print(text[0:len(text):6]) # сеикакл
print(text[::6]) # сеикакл
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
colors.append('gray') # добавить в конец
print(colors == ['red', 'green', 'blue', 'gray']) # True
colors.remove('red') #del colors[0] # удалить элемент

def function_name(x):
    return x**2
# body line 1
# . . .
# body line n
 # optional return

def f(x):
    if x == 1:
        return '÷елое'
    elif x == 2.3:
        return 23
    else:
        return

print(f(1)) # ÷елое
print(f(2.3)) # 23
print(f(28)) # None
print(type(f(1))) # str
print(type(f(2.3))) # int
print(type(f(28))) # NoneType
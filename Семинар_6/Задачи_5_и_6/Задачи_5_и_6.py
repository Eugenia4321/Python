#5 - Есть список случайных чисел в промежутке от 1 до 100, количеством 200. Создайте список кортежей, первый элемент которого - индекс элемента,
# а второй - сам элемент, при условии, что они не совпадают.
#[1,1,1,1] -> [(0,1),(1,1),(2,1),(3,1)] -> [(0,1),(2,1),(3,1)]

#6 - Из списка выше оставьте только те пары, где сумма кортежа кратна 5
#Пример
#[(10,25),(3,4),(4,1)] => [(10,25),(4,1)]

from random import randint

size= 200
max_num = 100
min_num = 1

input_list = [randint(min_num,max_num) for i in range(size)]
print(f'начальный список {input_list}')

result_list=list(filter(lambda result_list: result_list[1]!=result_list[0],enumerate(input_list)))
result_list1=list(filter(lambda result_list: (result_list[1]+result_list[0])%5==0,enumerate(input_list)))
print(f'спискок контежей с неповторяющимися элементами: {result_list}\n')
print(f'сумма кортежа кратна 5 :{result_list1}')


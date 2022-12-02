#3 - Дан массив размера N. После каждого отрицательного элемента массива вставьте элемент с нулевым значением.

#Пример:
#- пусть N = 4, тогда [28, -46, 14, -14] => [28, -46, 0, 14, -14, 0]

list_of_number = [28, -46, 14, -14]


def Add__zero_item(list_of_number):
    list_of_number_2 = []
    for i in range(len(list_of_number)):
        if int(list_of_number[i])<0:           
            list_of_number_2.append(list_of_number[i])
            list_of_number_2.append(0)
        else:
            list_of_number_2.append(list_of_number[i])
    return list_of_number_2

print(f'Start array {list_of_number}')
print(f'Final array {Add__zero_item(list_of_number)}')





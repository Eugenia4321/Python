




number_list = [2, 3, 5, 9, 3]

def Sum_odd_items(number_list):
    """
    Функция принимает список из целых чисел и возвращает сумму элементов на нечетной позиции с индексами 1,3,5...
    Arguments:
    (int) number_list[]
    Return:
    (int) result
    """
    result=0
    for i in range(1,len(number_list)):
        if i%2!=0:
            result+=number_list[i]
    return result 

print(f'Sum of odd items {number_list} is {Sum_odd_items(number_list)}')
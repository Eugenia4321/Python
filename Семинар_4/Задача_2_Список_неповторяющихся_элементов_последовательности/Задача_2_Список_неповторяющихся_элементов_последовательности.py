#2 - Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности. Не использовать множества.
#Постарайтесь решить за одно условие
#[1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]

from typing import List


input_list = [1,1,1,1,2,2,2,3,3,3,4]

def unique_items(input_list:List):
    """
    """
    input_list.sort()
    output_list =[]
    output_list.append(input_list[0])    
    for i in range(1,len(input_list)):
        if input_list[i-1] != input_list[i]:
            output_list.append(input_list[i])

    return output_list

print(f'{unique_items(input_list)}')
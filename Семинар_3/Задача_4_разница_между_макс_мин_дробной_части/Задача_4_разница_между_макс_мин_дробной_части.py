
list_of_numbers = [4.07, 5.1, 8.2444, 6.9814]

def difference_max_min_float_part(list_numb):
    """ Принимает массив вещественных чисел, возвращает разницу между максимальным и минимальным значением дробной части элементов.
    Arguments:
             (float)list_numb[]
        Return:
            (float) difference_max_min
    """
    fraction_part_list=[]
    for i in list_numb:        
        fraction_part_list.append(round(float(i)-int(i),10))
    difference_max_min = max(fraction_part_list)-min(fraction_part_list) 
    return difference_max_min


print(f'The difference between the maximum and minimum fractional part in the list {list_of_numbers} is {difference_max_min_float_part(list_of_numbers)}')






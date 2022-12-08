
number = int(input("Enter N = "))

def simple_multipliers(number:int) -> list:
    """ Принимает целое число, возвращает список множителей числа.
    Arguments:
             (int)number
        Return:
            (list)list_simple_multipliers
    """
    list_simple_multipliers=[]
    divider = 2
    while number >= divider:
        if number%divider == 0:
            list_simple_multipliers.append(divider)
            number = int(number / divider)
        else:
            divider+=1
    list_simple_multipliers.sort()
    return list_simple_multipliers

def delete_duplicates(input_array:list) -> list:
    """ Принимает список целых множителей, удаляет повторы , возвращает список уникальных множителей числа.
    Arguments:
             (list)input_array
        Return:
            (list)output_array
    """
    output_array=[]
    output_array.append(input_array[0])
    for i in range(1,len(input_array)):
        if input_array[i]!=input_array[i-1]:
            output_array.append(input_array[i])
    return output_array



print(f'{delete_duplicates(simple_multipliers(number))}')
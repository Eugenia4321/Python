



numbers_list = [2, 3, 4,  5, 6]

def product_numbers(numbers_list):
    """
    Принимает массив чисел и возращает массив из произведения пар чисел. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
    Arguments:
         (int) number_list[]
    Return:
          (int) result_list[]
    
    """
    result_list = []
    for i in range(0,int(len(numbers_list)/2)):
        result_item =numbers_list[i]*numbers_list[len(numbers_list)-1-i]
        result_list.append(result_item)
    if (len(numbers_list))%2!=0:
        result_list.append(numbers_list[int(len(numbers_list)/2)]**2)        
    return result_list

print(f'List: {numbers_list} \nResult list: {product_numbers(numbers_list)}')
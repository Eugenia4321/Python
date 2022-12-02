

from unittest import result


number_list = [2, 3, 5, 9, 3]

def Sum_odd_items(number_list):
    result=0
    for i in range(1,len(number_list)):
        if i%2!=0:
            result+=number_list[i]
    return result 

print(f'Sum of odd items {number_list} is {Sum_odd_items(number_list)}')
#2-  Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

1


int_list = list(map(int,input('Enter numbers:\n').split()))

if len(int_list)%2==0:
    len_result_list = len(int_list)/2
else:
    len_result_list = int(len(int_list)/2)+1

result_list = list(map(lambda i:(int_list[i]*int_list[-(i+1)]),[i for i in range(len_result_list)]))
print(f'input list {int_list}')
print(f'result list {result_list}')
from config import ERROR_MESSAGE,ERROR_MESSAGE_NOT_INT
import logging


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO, filename='py_log.log', filemode='w',encoding='UTF-8')

def check_digit(check_list:str)->bool:
    check_str=''
    for i in range(len(check_list)):
        check_str = str(check_list[i])
        #print(i,'  ',check_str)
        if not check_str.isdigit():
            logging.error(f'введены не числа "{check_list}"') 
            return False
    
    return True    
def check_count_numbers(list_num:list)->bool:
    if len(list_num)!=2:
        logging.error(f'количество чисел {len(list_num)} отличное от 2 в списке "{list_num}"')
        return False
    else:
        return True

def tele_sum(sum_list:list)->str:
    if check_digit(sum_list)==False:
        return ERROR_MESSAGE_NOT_INT
    if not check_count_numbers(sum_list):
        return ERROR_MESSAGE
    else:    
        result=int(sum_list[0]) +int(sum_list[1])
        return (f'{sum_list[0]} + {sum_list[1]} = {result}')


def tele_sub(sub_list:list)->str:
    if not check_digit(sub_list):
        return ERROR_MESSAGE_NOT_INT
    if not check_count_numbers(sub_list):
        return ERROR_MESSAGE
    else:    
        result=int(sub_list[0]) - int(sub_list[1])
        return (f'{sub_list[0]} - {sub_list[1]} = {result}')

def tele_div(div_list:list)->str:
    if not check_digit(div_list):
        return ERROR_MESSAGE_NOT_INT
    if not check_count_numbers(div_list):
        return ERROR_MESSAGE
    elif div_list[1]=='0':
        return ('Деление на 0? Не надо так :(')    
    else:    
        result=int(div_list[0]) /int(div_list[1])
        return (f'{div_list[0]} / {div_list[1]} = {result}')

def tele_mult(mult_list:list)->str:
    if not check_digit(mult_list):
        return ERROR_MESSAGE_NOT_INT
    if not check_count_numbers(mult_list):
        return ERROR_MESSAGE
    else:    
        result=int(mult_list[0]) *int(mult_list[1])
        return (f'{mult_list[0]} * {mult_list[1]} = {result}')
#example - пример 
example = ['-', '9', '-', '7', 'i', '/', '-', '1', '+', '1', 'i']
def tele_complex(complex_list:list= example) -> str:
    if len(complex_list)<1:
        return ERROR_MESSAGE 
    #так как разделение по пробелу - один пропущенный и все сломано. поэтому сначала лист в строку , потом строку в лист и работаем с ним
    complex_str = ''.join(complex_list)
    #удаляем лишнии символые если они есть
    complex_str=complex_str.replace(' ','')
    complex_str=complex_str.replace('(','')
    complex_str=complex_str.replace(')','')

    temp_complex_str = ''
    temp_complex_list = []
    #создаем новую строку с подходящим форматом
    for i in complex_str:
        if i.isdigit():
            temp_complex_str+=i
        else:
            temp_complex_list.append(temp_complex_str) 
            temp_complex_list.append(i)   
            temp_complex_str = ''
    #удаляем пустые элементы
    temp_complex_list = list(filter(None, temp_complex_list))
    # вставляем явный коэффициент если он был равен 1 и его пропустили 
    if temp_complex_list[2]=='i':
        temp_complex_list.insert(2,'1')
    if temp_complex_list[-2]=='+':
        temp_complex_list.insert(-1,'1')    
    #print(temp_complex_list) 
    #если коэфициенты были отрицательными числами - записываем в переменные отрицательные числа и удаляем лишнии знаки в списке через срезы
    #a1
    if temp_complex_list[0]=='-':
        a1 = int(temp_complex_list[1])*(-1)
        temp_complex_list=temp_complex_list[1:]
    else:
        a1 = int(temp_complex_list[0])
    #a2
    if temp_complex_list[4] in '/*-+' and  temp_complex_list[5] =='-':
        a2 = int(temp_complex_list[6])*(-1)
        temp_complex_list=temp_complex_list[:5]+temp_complex_list[6:]
       # print(temp_complex_list) 
    else:
        a2 = int(temp_complex_list[5])   
    #b1
    if temp_complex_list[1]=='-':
        b1=int(temp_complex_list[2])*(-1)
    else:
        b1=int(temp_complex_list[2])    
    #b2
    if temp_complex_list[6]=='-':
        b2 = int(temp_complex_list[7])*(-1)
    else:
        b2 = int(temp_complex_list[7])    
    #после приведения списка к виду [a1,+,b1,i,знак опецарии,а2,+,b2,i]должен остаться список из 9 элементов, если число другое  - пользователь ввел неверный пример, выводим сообщение об ошибке
    if len(temp_complex_list) !=9:
        logging.info(f'в вводе ошибка "{temp_complex_list}"') 
        return ERROR_MESSAGE 
    #вычисления     
    else:
        if temp_complex_list[4]=='+':
            result = (f'{a1+a2} + ({b1+b2}i)')            
        if temp_complex_list[4]=='-':
            result = (f'{a1-a2} + ({b1-b2}i)')
        if temp_complex_list[4]=='/':       
            #для деления берем дробные       
            a1 = float(a1)
            a2 = float(a2)
            b1 = float(b1)
            b2 = float(b2)
            result = (f' {(a1*a2+b1*b2)/(a2**2+b2**2)}+({(b1*a2-a1*b2)/(a2**2+b2**2)}i)')    
        if temp_complex_list[4]=='*':       
            result = (f' {a1*a2-b1*b2}+({a1*b2+b1*a2}i)') 
        #print(result)  
        logging.info(f'решено комплексное выражение"{temp_complex_list}" "{result}"') 
        return result
#tele_complex()
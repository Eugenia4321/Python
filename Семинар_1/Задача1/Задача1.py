
#1- Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
#Дополнительно: можете проверить, что это действительно число, и что это действительно входит в нужный диапазон

#Пример:

#6 -> да
#7 -> да
#1 -> нет

def Check_day_of_week(day_of_week):
    if 1>day_of_week or day_of_week>7:
        return 'wrong number'
    elif day_of_week==6 or day_of_week==7:
        return "yes"
    else:
        return 'no'
      
print(Check_day_of_week(int(input('Enter number = '))))


#1 - �������� ���������, ������� ��������� �� ���� ������������ ����� � ���������� ����� ��� ����. ������, ��� ����� ����� ���� ��������������

#������:

#67.82 -> 23
#(-0.56) -> 11


def Sum_of_digits(number):
    sum_of_digits = 0 
    for i in number:
        if i.isdigit():
            sum_of_digits+=int(i)
    return sum_of_digits



number = input('Enter number = ')
print(f'Sum of digits = {Sum_of_digits(number)}')


#2 - �������� ���������, ������� ��������� �� ���� ����� N � ������ ����� ������������ (����� - ��� ������) ����� �� 1 �� N.
#�� ����������� ������� math.factorial.

#������:
#- ����� N = 4, ����� [ 1, 2, 6, 24 ] #(1, 1*2, 1*2*3, 1*2*3*4)


def factorial_function(number):
    result = 1
    for i in range(1,number+1):
        result*=i
    return result

number = int(input('Enter number = '))
if number<=0:
    print('Error')
else:
    for i in range(1,number+1):
        print(factorial_function(i))


#1- �������� ���������, ������� ��������� �� ���� �����, ������������ ���� ������, � ���������, �������� �� ���� ���� ��������.
#�������������: ������ ���������, ��� ��� ������������� �����, � ��� ��� ������������� ������ � ������ ��������

#������:

#6 -> ��
#7 -> ��
#1 -> ���

def Check_day_of_week(day_of_week):
    if 1>day_of_week or day_of_week>7:
        return 'wrong number'
    elif day_of_week==6 or day_of_week==7:
        return "yes"
    else:
        return 'no'
      
print(Check_day_of_week(int(input('Enter number = '))))


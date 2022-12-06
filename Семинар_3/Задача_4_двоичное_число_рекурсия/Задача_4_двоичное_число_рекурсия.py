
def Bin_number(number, counter=0, result=0):
    """
    Принимает десятичное  число, переводчит его рекусивным методором в двоичное и возращает двоичное число
        Arguments:
             (int)number
             (int)counter
             (int)result

        Return:
            (int) result
    """
    result = result + number%2 * 10**counter
    if number<2:
        
        return result
    else:
       
        return Bin_number(int(number/2),counter+1,result)

number = int(input('Enter number = '))
bin_number = Bin_number(number,counter=0,result=0)
print(bin_number)

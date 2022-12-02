
def Bin_number(number, counter=0, result=0):
    if number<2:
        result = result + number%2 * 10**counter
        return result
    else:
        result = result + number%2 * 10**counter
        return Bin_number(int(number/2),counter+1,result)

number = int(input('Enter number = '))
bin_number = Bin_number(number,counter=0,result=0)
print(bin_number)

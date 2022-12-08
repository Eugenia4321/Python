
from ast import Str
from typing import List
#from unittest.util import strclass



def get_data_from_file(name_input_file : str ="unencrypted.txt") -> List:
    """
    """
    with open(name_input_file, "r") as input_file:
        input_data =input_file.read()   
           
    input_file.close()
    return input_data

def encryption_RLE(input_date:Str):
    """
    """
    char_count=1
    output_data=''
    for i in range(len(input_date)-1):
        if input_date[i]==input_date[i+1]:
            char_count+=1
        else:
            if char_count>1:
                output_data=output_data+str(char_count)
            output_data=output_data+input_date[i]
            char_count=1
        if i == len(input_date)-2:
            if char_count>1:
                output_data=output_data+str(char_count)
            output_data=output_data+input_date[i+1]
            
    return output_data 




def decryption_RLE(input_date:Str):
    output_data=''
    find_number_of_char=''
    for i in range(len(input_date)):        
        if input_date[i].isdigit():            
            find_number_of_char+=input_date[i]
        else:
            if find_number_of_char=='':
                find_number_of_char='1'
            for y in range(int(find_number_of_char)):
                output_data+=input_date[i] 
            find_number_of_char=''
    return output_data 

def writing_data_to_file(output_date:Str,name_output_file:Str ="unencrypted.txt"):
    """
    """
    with open(name_output_file, "w") as output_file:        
        output_file.write(output_date)
    output_file.close()    




print(f'unencrypted data: \n{get_data_from_file(name_input_file="unencrypted.txt")}\n')
print(f'encryption: {encryption_RLE(get_data_from_file())}\n')
writing_data_to_file(encryption_RLE(get_data_from_file()),name_output_file="encrypted.txt")
print(f'encrypted data: \n{get_data_from_file(name_input_file="encrypted.txt")}\n')
print(f'decrypted data: \n{decryption_RLE(get_data_from_file(name_input_file="encrypted.txt"))}\n')




from typing import List


example_input_text:str = 'бввб'
example_key:int=1
alphabet:str='абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ1234567890!";%:?*()_+,.'

def encryption_and_decryption(alphabet,example_input_text:str = 'бввб',key:int=1, key_status: bool = True):
    """ Принимает алфавит, текст для шифрования/дешифрования, ключ, булевую переменную для опредения действия с текстом - шифровать или расшифровать
        Возвращает зашифрованную/дешиврованную строку
    Arguments:
             (str)alphabet
             (str)example_input_text
             (int)key
             (bool)key_status
    Return:
            (str)output_text
        
    """
    output_text=''
    if not key_status:
        key=-key
    for i in range(0,len(example_input_text)):
        char = example_input_text[i]
        index_encrypted_char=alphabet.find(char)+key
        index_encrypted_char=index_encrypted_char%len(alphabet)
        output_text+=alphabet[index_encrypted_char]
    print(output_text)
    return output_text
#print(encryption_and_decryption(alphabet,example_input_text,key=1))

def writing_data_to_file(output_date:str,name_output_file:str ="encrypted.txt"):
    """ Принимает строку данных и строку с называнием файла, открывает файл и перезаписывает строку с данными в него.
    Arguments:
             (str)output_date
             (str)name_output_file
        
    """
    with open(name_output_file, "w") as output_file:        
        output_file.write(output_date)
    output_file.close()    

def get_data_from_file(name_input_file : str ="encrypted.txt") -> List:
    """ Принимает строку с называнием файла, открывает файл, и возвращает считанную строку.
    Arguments:
             (str)name_input_file
       
    """
    with open(name_input_file, "r") as input_file:
        input_data =input_file.read()   
           
    input_file.close()
    return input_data

key = int(input('Enter key:\n'))
key_status_str = input('Entet 1 to encrypt the text or enter 2 to decrypt the text \n')
if key_status_str=='1': #зашифровать
    key_status=True    
    example_input_text = input('Enter text:\n')
    writing_data_to_file(encryption_and_decryption(alphabet,example_input_text,key,key_status))

else:   #расшифровать
    key_status=False
    print(encryption_and_decryption(alphabet,get_data_from_file(),key, key_status))
    






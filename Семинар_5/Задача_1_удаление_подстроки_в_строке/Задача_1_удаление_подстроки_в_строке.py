#1-Напишите программу, удаляющую из текста все слова, содержащие заданную строку.

#Пример:
#Пугать ты галок пугай => заданная строка "галок" => Пугать ты пугай
#Пугать ты галок пугай => заданная строка "пуг" => Пугать ты галок

input_data = list(input('Enter text:\n').split())
input_word = input('Enter word:\n')

def delete_word(input_data:list,input_word:str) -> str:
    """
    """
    output_text=''
    for i in range(0,len(input_data)):
        if str(input_data[i]).find(input_word) == -1:
            output_text+=input_data[i]+' '
          
    return output_text

print(delete_word(input_data,input_word))
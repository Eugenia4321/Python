#1- Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
#Примеры
#список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
#список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
#список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
#список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
#список: [], ищем: "123", ответ: -1


input_list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
find_item = "qwe"

def find_second_occurence(input_list: list[str], search_word: str) -> int:
    try:
        list_indexes = [index for index, string in enumerate(input_list) if string == search_word]
       
        return list_indexes[1]
    except IndexError:
        return -1

print(f'второе вхождение элемента {find_item} в списке {input_list} на позиции {find_second_occurence(input_list,find_item)}')
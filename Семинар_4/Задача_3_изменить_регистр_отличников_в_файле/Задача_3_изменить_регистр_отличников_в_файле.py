





from typing import List


def get_list_of_students(name_performance_file : str ="performance.txt") -> List:
    """ Принимает строку с названием файла, открывает файл, считывает данные и записываетпострочко в списко, возвращает список
    Arguments:
             (str)name_performance_file
        Return:
            (list)academic_performance
    """
    with open(name_performance_file, "r") as file_academic_performance:
        for line in file_academic_performance.readlines():
            academic_performance.append(line)
    file_academic_performance.close()
    return academic_performance

def change_register(academic_performance : List[str])-> List:
    """ Принимает список строк, изменяет регистры на верхний у людей с оценкой выше 5, возращает изменненый список строк
    Arguments:
             (list)academic_performance 
        Return:
            (list)academic_performance
    """
    for i in range(len(academic_performance)-1):
        academic_record=academic_performance[i]
        for char in academic_record:
            if char.isdigit():
                if int(char) > 4:
                    academic_performance[i] = academic_record.upper()
    return academic_performance

def overwriting_list_of_students(academic_performance: list,name_performance_file: str="performance.txt"):
    """ Принимает список строк и строку с названием файла ,перезаписывает список строк в файл.
    Arguments:
             (list)academic_performance
             (str)name_performance_file
       
    """
    with open(name_performance_file, "w") as output_file_academic_performance:
        for i in range(len(academic_performance)):
            output_file_academic_performance.write(academic_performance[i])
    output_file_academic_performance.close()


academic_performance = []
academic_performance=get_list_of_students()
print(academic_performance)
change_register(academic_performance)
overwriting_list_of_students(academic_performance,name_performance_file="performance.txt")
print(academic_performance)

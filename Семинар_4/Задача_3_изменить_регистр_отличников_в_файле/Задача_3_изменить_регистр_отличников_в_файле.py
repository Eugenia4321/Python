





from typing import List


def get_list_of_students(name_performance_file : str ="performance.txt") -> List:
    """
    """
    with open(name_performance_file, "r") as file_academic_performance:
        for line in file_academic_performance.readlines():
            academic_performance.append(line)
    file_academic_performance.close()
    return academic_performance

def change_register(academic_performance : List[str])-> List:
    """
    """
    for i in range(len(academic_performance)-1):
        academic_record=academic_performance[i]
        for char in academic_record:
            if char.isdigit():
                if int(char) > 4:
                    academic_performance[i] = academic_record.upper()
    return academic_performance

def overwriting_list_of_students(academic_performance: list,name_performance_file: str="performance.txt"):
    """
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

#2- Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
#Нужно написать таблицу истинности.


# решение исходят из предположения что всё таки там нужны вторые скобки и задача выглядит ¬(X ⋁ Y ⋁ Z) = (¬X ⋀ ¬Y ⋀ ¬Z)
def it_was_misstake_to_start_learn_programming():
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0,2):
                print(f'x = {x}, y = {y}, z = {z} : ¬(X ⋁ Y ⋁ Z) = (¬X ⋀ ¬Y ⋀ ¬Z) is {not(x or y or z) == ((not x) and (not y) and (not z))}')


it_was_misstake_to_start_learn_programming()
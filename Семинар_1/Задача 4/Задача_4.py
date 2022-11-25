#4-Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
#Пример:
#- quarter = 1 => x∈(0, ∞) u y∈(0,∞)

def Check_coordinates(quarter):
    if quarter>4 or quarter< 1:
        print('does not exist')
    if quarter == 1:
        print('x∈(0, ∞) u y∈(0, ∞)')
    if quarter == 2:
        print('x∈(∞, 0) u y∈(0, ∞)')
    if quarter == 3:
        print('x∈(∞, 0) u y∈(∞, 0)')
    if quarter == 4:
        print('x∈(0, ∞) u y∈(∞, 0)')



Check_coordinates(int(input('quarter = ')))



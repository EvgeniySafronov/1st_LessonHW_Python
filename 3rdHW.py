""" Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
    в которой находится эта точка (или на какой оси она находится).

Пример:

- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3 """

x = int(input('Введите координаты по оси Х: '))
y = int(input('Введите координаты по оси Y: '))
if x > 0 and y > 0:
    print(f'{1} четверть')
if x < 0 and y > 0:
    print(f'{2} четверть')
if x < 0 and y < 0:
    print(f'{3} четверть')
if x > 0 and y < 0:
    print(f'{4} четверть')
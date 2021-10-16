'''Андре Септиянто - Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.'''

from sys import argv

if len(argv) < 4:
   print(f'input data (productivity, salary per hour, Bonuses)!')
else:
    a = float(argv[1])
    b = float(argv[2])
    c = float(argv[3])
    result = a * b + c
    print(argv)
    print(result)

'''Aндре септиянто - Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.'''


def summary():
    try:
        with open('file_5.txt', 'w+') as file:
            line = input('Введите цифры через пробел \n')
            file.writelines(line)
            my_number = line.split()

            print(sum(map(int, my_number)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Неправильно набран номер. Ошибка ввода-вывода')

summary()
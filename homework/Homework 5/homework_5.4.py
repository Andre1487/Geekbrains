'''Aндре септиянто - Создать (не программно) текстовый файл со следующим содержимым:

One — 1

Two — 2

Three — 3

Four — 4

Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.'''


rus = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}

with open('file_4.txt', 'r') as file, open('file_4_new.txt', 'w') as file_new:
    file_lines = file.readlines()
    for line in file_lines:
        data = line.split(' ', 1)
        rus_num = rus.get(data[0])
        file_new.write(f'{line.replace(data[0], rus_num)}')

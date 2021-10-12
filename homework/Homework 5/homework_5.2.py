'''Aндре септиянто - Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.'''

with open('homework5.txt') as file:
    file_lines = file.readlines()
    str_count = 0
    for num, line in enumerate(file_lines):
        str_count += 1
        words_count = len(line.split())
        print(f'#{num + 1} - {words_count} Words')
    print(f'{str_count} strokes!')
'''септиянто Андре - 2. Для списка реализовать обмен значений соседних элементов,
 т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
 При нечетном количестве элементов последний сохранить на своем месте.
 Для заполнения списка элементов необходимо использовать функцию input().'''

user_input = input("List: ")
input_list = user_input.split()
len_list = len(user_input.split())
i = 0
if len_list > 1:
    while i < len_list - 1 :
        input_list[i], input_list[i + 1] = input_list[i + 1], input_list[i]
        i += 2

print(input_list)
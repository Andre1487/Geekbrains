'''Андре септиянто - Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.'''
def my_func(arg1 , arg2, arg3):
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg1 >= arg2 and arg1 <= arg3:
        return arg1 + arg3
    elif arg2 >= arg1 and arg1 <= arg3:
        return arg2 + arg3
    else:
        return arg3 + arg2

print(f'Result - {my_func(int(input("enter first argument: ")), int(input("enter second argument: ")), int(input("enter third argument: ")))}')
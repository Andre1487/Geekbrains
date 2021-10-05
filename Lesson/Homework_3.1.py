# '''Андре Септиянто - Реализовать функцию, принимающую два числа позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.'''

def division(*arg):

    try:
        arg1 = int(input("Input number 1 "))
        arg2 = int(input("Input number 2 "))
        result = arg1 / arg2
    except ValueError:
        return ('Value error')
    except ZeroDivisionError:
        return ("Wrong devider! You can't use zero as a devider")

    return result

print(f'result  {division()}')
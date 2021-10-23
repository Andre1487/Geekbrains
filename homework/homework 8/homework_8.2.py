"""Андре септиянто - Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя
программа должна корректно обработать эту ситуацию и не завершиться с ошибкой."""


class ZeroDivisionError(Exception):
    text = "division by zero is not allowed"

    def __str__(self):
        return self.text


class Number(float):
    def __truediv__(self, other):
        if other is not None and not other:
            raise ZeroDivisionError

        return Number(float(self) / float(other))


if __name__ == '__main__':
    while True:
        try:
            dividend, divider = map(Number, input("please input dividend and divider number by space: ").split())
            print(dividend / divider)
        except ZeroDivisionError as e:
            print(e)
        except ValueError as e:
            print(e)
            break

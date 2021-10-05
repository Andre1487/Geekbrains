'''Андре Септиянто - Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных
 о пользователе одной строкой.'''


def my_func (name, surname, year, city, email, telephone):
    return ' - '.join([name, surname, year, city, email, telephone])

print(my_func(surname = 'Septiyanto', name = 'andre', year = '1987', city = 'Spb', email = 'andre@yahoo.com', telephone = '89213456788'))
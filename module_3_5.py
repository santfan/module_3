# Объявим функцию
def get_multiplied_digit(numbers):
    # Преобразуем число в строку
    str_numbers = str(numbers)
    # Получим первую цифру
    first = int(str_numbers[0])
    # Посмотрим что в стеке вызова
    print(f'Длина строковой переменной в стеке вызова {len(str_numbers)}')
    print(f'Цифра которая находится в стеке вызова {first}')
    # Зададим условия вызова рекурсивной функции
    if len(str_numbers) > 1:
        return first * get_multiplied_digit(int(str_numbers[1:]))
    # Выход из рекурсии
    else:
        return first  # Это последнее число рекурсии и первое в стеке вызова
# Вызовем функцию с вводом числа и отбразим результат работы рекурсии
print(get_multiplied_digit(int(input())))
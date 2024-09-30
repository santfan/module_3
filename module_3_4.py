# Объявим функцию
def single_root_words(root_words, *other_words):
    # Установим пустой список, в который будем складывать результаты
    same_words = []
    # Организуем цикл
    for word in other_words:
        # Зададим условия проверки
        if root_words.lower() in word.lower() or word.lower() in root_words.lower():
            # Добавим слова отвечающие условию
            same_words.append(word)
    # Преобразуем кортеж в список и вернем результат работы функции
    return list(same_words)

# Вызовем функцию с параметрами объявленными переменными
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
# Отобразим результаты работы функции
print(result1)
print(result2)
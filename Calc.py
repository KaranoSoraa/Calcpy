while True:
    print("Введите первое число:")

    try:
        x = float(input())
    except ValueError:
        print("Введен не верный параметр.")
        continue

    print("Введите второе число:")
    try:
        y = float(input())
    except ValueError:
        print("Введен не верный параметр.")
        continue

    print("Введите операцию: (сум, выч, дел, умн, степ, кор)")
    z = input()

    if z == "сум" or z == "Сум" or z == "СУМ":
        print(x + y)
    elif z == "выч" or z == "Выч" or z == "ВЫЧ":
        print(x - y)
    elif z == "дел" or z == "Дел" or z == "ДЕЛ":
       if y != 0:
           print(x / y)
       else:
           print("Попытка деления на ноль. Введите другие значения.")
    elif z == "умн" or z == "Умн" or z == "УМН":
        print(x * y)
    elif z == "степ" or z == "Степ" or z == "СТЕП":
        print(x ** y)
    else:
        print("Не корректное условие")

    print("Хотите продолжить? (Да или нет)")
    a = input()
    if a == "Нет" or a == "нет":
        print("Завершение программы.")
        break

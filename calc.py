#Простой калкьуклятор, на питоне я особо не пишу, просто знаком. Сделал при помощи ресерча в интернете.

def calculate():
    expression = input("Введите математическое выражение: ")
    try:
        result = eval(expression)
        print("Результат: ", result)
    except Exception as e:
        print("Ошибка: ", str(e))

calculate()

__author__ = 'Андрей Герасимов'
# Программа показывает алгоритм рекурсии. Требуется рассчитать произведение всех цифр числа

def get_multiplied_digits(number):
    while number%10 == 0:   # данный цикл выполняется до тех пор, пока все возможные нули в конце числа не уберутся
        number = number//10
    str_number = str(number)
    first = int (str_number[0]) # приводя к целому, убираем возможные нули в начале числа

    if len (str_number) > 1:
        return (first * get_multiplied_digits(int(str_number[1:])))
    else:
        return (first)

Result = get_multiplied_digits(4020300)
print(Result)

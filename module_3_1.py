__author__ = 'Андрей Герасимов'

calls = 0 #== глобальный счетчик вызовов функции

def count_calls (): # функция увеличения глобального счетчика
    global calls
    calls+=1

def string_info (a):
    count_calls()
    leng = len(a)
    up=a.upper()
    low=a.lower()
    return((leng,up,low)) # функция возвращает кортеж из длины этой строки,
                          # строку в верхнем регистре, строку в нижнем регистре.

def is_contains (string , list_to_search):#функция для проверки находится ли строка в списке
    count_calls()
    lowstring = string.lower() #приведение к одному регистру
    low_list =[]
    for i in list_to_search:
        low_list.append(i.lower()) #приведение к одному регистру


    if lowstring  in low_list : # проверка, находится ли строка в списке
        return (True)
    else:
        return (False)


for j in range(3):
    print(string_info('zeBra'))

for k in range(5):
    print(is_contains('Zebra', ['zebra','kozel','copybara']))

print('Количество вызовов функций', calls)

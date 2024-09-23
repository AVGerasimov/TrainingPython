__author__ = 'Андрей Герасимов'

def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

# Различные виды принтаутов
print_params()
print_params(3)
print_params(4, 5)
print_params(4, 5, 6)
print_params(b=25)
print_params(c=[1,2,3])


values_list = [1, True, 'Urban']           #Списокдля распаковки
values_dict = {'a' : 1, 'b' : 2, 'c':3}    #Словарь для распаковки

print_params(*values_list) #Распаковка списка
print_params(**values_dict) #Распаковка словаря

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42) #Распаковка списка в первые два параметра
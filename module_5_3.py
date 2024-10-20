__author__ = 'Андрей Герасимов'

class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if (new_floor>0) and (new_floor<self.number_of_floors+1):
            for i in range(1, new_floor+1):
                print(i)
        else:
            print('Такого этажа не существует')

    def __len__(self):
        return(self.number_of_floors)

    def __str__(self):
        return (f'Название: {self.name} кол-во этажей: {self.number_of_floors}')

# методы перегрузки операторов для сравнения и арифметических операций с учетом количества этажей
    def __eq__(self, other):
        if isinstance(other, House):
            return (self.number_of_floors == other.number_of_floors) # должен возвращать True, если количество этажей одинаковое у self и у other

    def __lt__(self, other):
        if isinstance(other, House):
            return (self.number_of_floors < other.number_of_floors) # должен возвращать True, если количество этажей  self меньше чем other

    def __le__(self, other):
        if isinstance(other, House):
            return (self.number_of_floors <= other.number_of_floors) # должен возвращать True, если количество этажей  self меньше или равно  other

    def __gt__(self, other):
        if isinstance(other, House):
            return (self.number_of_floors > other.number_of_floors) # должен возвращать True, если количество этажей  self больше  other

    def __ge__(self, other):
        if isinstance(other, House):
            return (self.number_of_floors >= other.number_of_floors) # должен возвращать True, если количество этажей  self больше или равно  other

    def __ne__(self, other):
        if isinstance(other, House):
            return (self.number_of_floors != other.number_of_floors)  # должен возвращать True, если количество этажей  self не равно  other




# Перегрузка четырех основных математических операторов

    def __sub__(self, other):
        if isinstance(other, int):
            self.number_of_floors-=other
            return (self)


    def __mul__(self, other):
        if isinstance(other, int):
            self.number_of_floors*=other
            return (self)

    def __truediv__(self, other):
        if isinstance(other, int):
            self.number_of_floors/=other
            return (self)

    def __add__(self, other):
        if isinstance(other, int):
            self.number_of_floors+=other
            return (self)


#   Методы __iadd__ и __radd__ не обязательно описывать заново, достаточно вернуть значение вызова __add__
    def __iadd__(self, other):
        return (self+other)


    def __radd__(self, other):
        return (self+other)




h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__





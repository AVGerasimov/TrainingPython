__author__ = 'Андрей Герасимов'

class Vehicle:
    __COLOR_VARIANTS = ['BLUE', 'RED', 'GREEN', 'BLACK', 'WHITE']


    def __init__(self, owner, model, engine_power, color ):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color




    def get_model(self):   #- возвращает строку: "Модель: <название модели транспорта>"
        return('Модель: '+self.__model)

    def get_horsepower(self):
        return('Мощность двигателя: '+str(self.__engine_power))

    def get_color(self):   #- возвращает строку: "Модель: <название модели транспорта>"
        return('Цвет: '+self.__color)

    def print_info(self):
        print(f'Модель: {self.__model}')
        print(f'Мощность двигателя: {self.__engine_power}')
        print(f'Цвет: {self.__color}')
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):
        if new_color.upper() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')



class Sedan (Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Fedos', 'Toyota Mark II',  500, 'blue')
# Изначальные свойства
vehicle1.print_info()

#Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()





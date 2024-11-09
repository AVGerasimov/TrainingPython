__author__ = 'Андрей Герасимов'


class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message

class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message



class Car:
    def __init__(self, model ,__vin , __numbers ):
        self.model = model
        self.__vin = __vin
        self.__numbers = __numbers



        def __is_valid_vin(vin_number):
            if isinstance(vin_number, int)== False:
                raise IncorrectVinNumber ('Некорректный тип vin номер')
            if vin_number not in range(1000000,9999999):
                raise IncorrectVinNumber('Неверный диапазон для vin номера')
            else:
                return True



        def __is_valid_numbers(numbers):
            if isinstance(numbers, str) == False:
                raise IncorrectCarNumbers('Некорректный тип данных для номеров')
            if len(numbers) !=6:
                raise IncorrectCarNumbers('Неверная длина номера')
            else:
                return True

        __is_valid_vin(self.__vin)
        __is_valid_numbers(self.__numbers)




try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')




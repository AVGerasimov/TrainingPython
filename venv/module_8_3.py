__author__ = 'Андрей Герасимов'

class Car:
    def __init__(self, model ,__vin , __numbers ):
        self.model = model
        self.__vin = __vin
        self.__numbers = __numbers



        def __is_valid_vin(vin_number):
            if isinstance(vin_number, int)== False:
                raise NameError ('Некорректный тип vin номер')
            if vin_number not in range(1000000,9999999):
                raise NameError('Неверный диапазон для vin номера')

        __is_valid_vin(self.__numbers)

        def __is_valid_numbers(numbers):
            pass


try:
    first = Car('Model1', 1000001, 'f123dj')

except NameError as exc1:
    print(f'wow {exc1}   {type(exc1)}')
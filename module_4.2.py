__author__ = 'Андрей Герасимов'

def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()
    pass


test_function()

try:
    inner_function()
except:
    print("this is wrong call")
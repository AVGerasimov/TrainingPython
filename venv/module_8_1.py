__author__ = 'Андрей Герасимов'

def add_everything_up (a, b):
    try:
        c=a+b
        return "{:.3f}".format(c)
    except(TypeError):
        return str(a)+str(b)
    except:
        print('Fault')
        return ('Fault')


print(add_everything_up(123.456, 'строка').format())
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))






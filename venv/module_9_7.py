__author__ = 'Андрей Герасимов'

def is_prime(sum_three):
    def wrapper(a, b, c):
        originalfunc = sum_three(a, b, c)
        rs = originalfunc
#  ======= Проверка ,является ли результат суммы простым или составным=====
        k = 0
        for i in range(2, rs // 2 + 1):
            if (rs % i == 0):
                k = k + 1
        if (k <= 0):
            print("Простое")
        else:
            print("Составное")
#  ========================================================================
        return originalfunc
    return wrapper

@is_prime
def sum_three(x1, x2, x3):
    return x1+x2+x3



result = sum_three(2, 3, 6)
print(result)
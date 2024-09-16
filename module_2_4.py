__author__ = 'Андрей Герасимов'
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] #исходный список
primes = []
not_primes = []

for i in numbers: #перебор исходного списка
    is_prime = True # переменная-флаг
    if i > 1: #только если число больше 1 оно может быть простым или составным
        for j in range(2, i): #перебор делителей.
            if i%j == 0:
                is_prime = False#делитель найден, значит число не является простым
                break #если делитель найден,выходим из цикла

        if is_prime== True: # если число простое, добавляем его в список простых
            primes.append(i)
        else:  # если число составное, добавляем его в список составных
            not_primes.append(i)
print("prime", primes)
print("not prime", not_primes)

# new comment

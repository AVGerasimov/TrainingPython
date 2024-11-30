import threading
import time
import random

class Bank(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.balance = 0 #начальное значение баланса в банке
        self.lock = threading.Lock() #создание объекта блокировки потоков
        self.lock.acquire()# так как начальный баланс нулевой, стоит блокировка на снятие

    def deposit(self):
        transact = 0
        while transact<100:
            add = random.randint(50, 500)
            print(f' Запрос на пополнение {add}')
            if self.balance <= 500 and self.lock.locked() == True: #если баланса недостаточно и было снятие денег, пополняем
                self.balance+= add
                self.lock.release()  # замок открывается, баланс пополнен
                print(f"Пополнение: {add}. Баланс: {self.balance}")
            transact+=1
            time.sleep(0.01)


    def take(self):
        transact = 0
        while transact<100:
            sub = random.randint(50, 500)
            print(f' Запрос на снятие {sub}')
            if sub > self.balance:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()  # замок закрывается , когда происходит попытка снятия при недостаточном балансе.
            else:
                self.balance-= sub
                print(f"Снятие: {sub}. Баланс: {self.balance}")
            transact+=1
            time.sleep(0.01)

bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')

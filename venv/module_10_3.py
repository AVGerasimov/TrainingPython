import threading
import time
import random

class Bank(threading.Thread):
    def __init__(self, balance):
        threading.Thread.__init__(self)
        self.balance = balance
        self.lock = threading.Lock()


    def deposit(self):
        transact = 0
        while transact<100:
            add = random.randint(50, 500)
            print(f' Запрос на добавку {add}')
            if self.balance <= 500 and self.lock.locked() == True:
                if self.lock.locked() == True:
                    self.lock.release()  # замок открывается
                self.balance+= add
                print(f"Пополнение: {add}. Баланс: {self.balance}")
            transact+=1
            time.sleep(0.001)


    def take(self):
        transact = 0
        while transact<100:
            sub = random.randint(50, 500)
            print(f' Запрос на {sub}')
            if sub > self.balance:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()  # замок закрывается
            else:
                self.balance-= sub
                print(f"Снятие: {sub}. Баланс: {self.balance}")
            transact+=1
            time.sleep(0.001)

bk = Bank(0)

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')

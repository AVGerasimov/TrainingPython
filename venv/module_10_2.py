import threading
import time
import datetime

class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.enemy = 100
        self.day_of_battle = 0

    def run(self):
        print(f'{self.name}, на нас напали! \n')
        while self.enemy>0:
            self.day_of_battle += 1
            self.enemy = self.enemy - self.power
            print(f'{self.name} сражается {self.day_of_battle} день(дня), осталось {self.enemy} воинов.')
            time.sleep(1)
        print(f'{self.name} одержал победу спустя {self.day_of_battle} дней(дня)!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
print('Все битвы закончились!')


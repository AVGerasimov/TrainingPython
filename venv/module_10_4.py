__author__ = 'Андрей Герасимов'

import threading
import time
import datetime
import random
from queue import Queue

class Table:
    def __init__(self,numbs):
        self.numbs = numbs
        self.guest = None



class Guest(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        waits = random.randint(3, 10)
        time.sleep(waits)



class Cafe:
    def __init__(self, *args):
        self.tables = []
        for i in args:
            self.tables.append(i)
        self.queue = Queue()

    def guest_arrival(self, *guests):
 #       print(f"Пуста ли очередь - {self.queue.empty()}")
# получив список гостей, начинаем назначать им столы
        for j in guests:
        #проверка свободны ли столы
            AssignSucsecc = False #случилось ли назначение стола
            NumberTable = 0
            for i in tables:
                NumberTable+=1 #номер стола
                if i.guest == None : #пробегая по столам, как только находим пустой, сразу назначаем гостя
                    i.guest = j  #назначение гостя
                    print(f"{j.name} сел(-а) за стол номер {NumberTable}")
                    AssignSucsecc = True
                    # так как назначение случилось, запускаем поток гостя
                    j.start()
                    break# назначение случилось, сразу выходим из цикла
                #если же , пробежав по всем столам, мы так и не нашли свободного,то
            if AssignSucsecc == False:
                print(f"{j.name} в очереди")
        #  помещение гостя в очередь
                self.queue.put(j)
 #       print(f"Пуста ли очередь - {self.queue.empty()}")



    def discuss_guests(self):

#   проверяем, есть ли занятые столы
        BusyTable = False
        for i in tables:
            if i.guest != None:
                BusyTable = True#если хотя бы один занят

        while self.queue.empty()==False or BusyTable == True :        #Обслуживание должно происходить пока очередь не пустая (метод empty) или хотя бы один стол занят
            for i in self.tables:
                if  i.guest != None:
                    if i.guest.is_alive() == False:
                        print(f'{i.guest.name} покушал(-а) и ушёл(ушла)')
                        i.guest = None
                        print(f'Стол номер {i.numbs} свободен')
                        if self.queue.empty()==False:#== если очередь не пуста, садим гостя за стол
                            i.guest = self.queue.get()
                            print(f"{i.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {i.numbs}")
                            i.guest.start()
            BusyTable = False
            for j in self.tables:
                if j.guest != None:
                    BusyTable = True  # если хотя бы один занят



# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]

# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()

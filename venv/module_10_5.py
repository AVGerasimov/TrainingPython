import time
import multiprocessing
from multiprocessing import Process
from multiprocessing import Pool


def  read_info(name):
    all_data = []
    with open (name,'r', encoding='utf-8') as file:
        line = file.readline()
        all_data.append(line)
        while line != '':
            line = file.readline()
            if line != '':
                all_data.append(line)
    print(f" прочитан файл номер {file.name}")
    return all_data


filenames = [f'./file {number}.txt' for number in range(1, 5)]

# t1 = time.time()
# print(f' Начало линейного способа, время = {t1}')
# for i in range(1, 5):
#     read_info(filenames[i-1])
#     print(f" прочитан файл номер {i-1}")
# t2 = time.time()
# print(t2)
# delta = t2-t1
# print(f' время линейный способ чтения, результат = {delta}')


t1 = time.time()
print(f' Начало многопроцессорного способа, время = {t1}')
if __name__ == '__main__':
    # Создание пула из 4 процессов
    with Pool(processes=4) as pool:
        # Входной список значений
        # Применение функции read_info к каждому элементу в списке параллельно
        results = pool.map(read_info, filenames)

t2 = time.time()
print(f' Конец многопроцессорного способа, время = {t2}')
delta = t2-t1
print(f' Время многопроцессорный способ чтения = {delta}')






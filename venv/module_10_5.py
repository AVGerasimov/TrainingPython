import time
from multiprocessing import Pool


def read_info(name):
    start_time = time.time()
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        line = file.readline()
        all_data.append(line)
        while line != '':
            line = file.readline()
            if line != '':
                all_data.append(line)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Файл {name} прочитан за {elapsed_time:.3f} с.")
    return all_data


filenames = [f'./file {number}.txt' for number in range(1, 5)]



t1 = time.time()
print(f' Начало линейного способа, время = {t1}')
for i in range(1, 5):
    read_info(filenames[i-1])
    print(f" прочитан файл номер {i-1}")
t2 = time.time()
print(t2)
delta = t2-t1
print(f' время линейный способ чтения, результат = {delta}')




if __name__ == '__main__':
    t1 = time.time()
    print(f'Начало многопроцессорного способа, время = {t1:.3f} с.')

    with Pool(processes=4) as pool:
        results = pool.map(read_info, filenames)

    t2 = time.time()
    delta = t2 - t1
    print(f'Конец многопроцессорного способа, время = {t2:.3f} с.')
    print(f'Общее время многопроцессорного способа чтения: {delta:.3f} с.')
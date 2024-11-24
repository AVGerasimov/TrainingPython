import threading
import time
import datetime

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count+1):
            file.write('Какое-то слово № '+str(i)+'\n')
            time.sleep(0.1)
        print(f"Завершилась запись в файл {file_name}")

current_time = datetime.datetime.now().time()
xcurrent_time = time.time()
print(current_time)

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

current_time1 = datetime.datetime.now().time()
xcurrent_time1 = time.time()
print(f'Работа потоков {current_time1}')
print(f'Время выполнения первых четырех функций {xcurrent_time1-xcurrent_time} сек')

print(threading.main_thread())


thread1 = threading.Thread(target=write_words, args = (10, 'example5.txt'))
thread1.start()


thread2 = threading.Thread(target=write_words, args = (30, 'example6.txt'))
thread2.start()


thread3 = threading.Thread(target=write_words, args = (200, 'example7.txt'))
thread3.start()

thread4 = threading.Thread(target=write_words, args = (100, 'example8.txt'))
thread4.start()



thread1.join()
thread2.join()
thread3.join()
thread4.join()

print('Все потоки завершены')
xcurrent_time2 = time.time()
print(current_time)
print(f'Время выполнения  четырех потоков {xcurrent_time2-xcurrent_time1} сек')

print(threading.enumerate())
__author__ = 'Андрей Герасимов'

def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding = 'utf-8')
    strings_positions  = dict()
    key = tuple()
    for index,i in enumerate(strings):
        key = (index+1,file.tell())
        file.write(i + '\n')
        strings_positions [key] = i
    return (strings_positions)
    file.close()



info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
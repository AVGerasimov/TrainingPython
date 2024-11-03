__author__ = 'Андрей Герасимов'

class WordsFinder:
    file_names = [] #все переданные названия файлов в конструкторе помещаются в это список
    def __init__(self, *params):
        for i in params:
            self.file_names.append(i)

    def getter(self):
        return(self.file_names)

    def get_all_words(self): #метод возвращает словарь из названий файлов (ключи) и значений
        all_words = dict()
        mylist = []
        myText = ""
        for i in self.file_names:
            with open(i, encoding = 'utf-8') as file:
                for linexxx in file:
                    myline = linexxx.lower()
                    myline = myline.replace(",","").replace(".","").replace("=","").replace("!","").replace("?","")\
                    .replace(";", "").replace(":", "").replace("-", "")
                    myText = myText + myline
            mylist = myText.split()
            all_words[i] = mylist
            myText = ""
        return (all_words)

    def find(self, word):
        final_pos = dict()  # для выдачи результата
        temp = self.get_all_words()
        # поочередно перебирая ключи из словаря temp найдем первое попавшееся слово word и запомним его позицию
        for name, words in temp.items():
            for index, value in enumerate(words):
                if value == word:
                    final_pos[name] = index+1
                    break
                else:
                    final_pos[name] = 0
        return final_pos

    def count(self, word):
        final_pos = dict()  # для выдачи результата
        temp = self.get_all_words()
        # поочередно перебирая ключи из словаря temp увеличиваем summ если находим слово word
        for name, words in temp.items():
            summ =0
            for  value in words:
                if value == word:
                    summ+=1
            final_pos[name] = summ
        return final_pos



finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))



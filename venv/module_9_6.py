__author__ = 'Андрей Герасимов'


def  all_variants(text):
    for dlina in range(0, len(text)): #= dlina - длина подпоследовательности
            i = 0
            while i != len(text)-dlina:
                yield text[i:i+dlina+1]
                i += 1


a = all_variants("abc")
print(a)
for i in a:
    print(i)
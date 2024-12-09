import matplotlib.pyplot as plt
import requests
import sys
import pandas as pd


print("Демонстрация библиотеки matplotlib, построение графика")
squares = [1, 4, 9, 16, 25]
cub = [1, 8, 27, 64, 25]
fig, ax = plt.subplots()
ax.plot(squares, linewidth=3)
ax.set_title('Graphics', fontsize=18)
ax.plot(cub, linewidth=2)
plt.show()





print("Демонстрация библиотеки requests, получение данных от погоде в г. Томск")
s_city = "Томск"
appid = "5c0a770a8be4f2e894db4eb5995e2065"
city_id = 1489421
print(f'Текущая погода в городе {s_city}:')
try:
    res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                 params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    data = res.json()
    print("conditions:", data['weather'][0]['description'])
    print("temp:", data['main']['temp'])
    print("temp_min:", data['main']['temp_min'])
    print("temp_max:", data['main']['temp_max'])
except Exception as e:
    print("Exception (weather):", e)
    pass


print("Демонстрация библиотеки pandas")
print("Структура/объект Series представляет из себя объект, похожий на одномерный массив (питоновский список, например),\n но отличительной его чертой является наличие ассоциированных меток")
my_series = pd.Series([5, 6, 7, 8, 9, 10])
print(my_series)

print('DataFrame является табличной структурой данных')
df = pd.DataFrame({'country': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine'],
 'population': [17.04, 143.5, 9.5, 45.5],
 'square': [2724902, 17125191, 207600, 603628]})

print(df)
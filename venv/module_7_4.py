__author__ = 'Андрей Герасимов'

team1_num = 5
print("В команде Мастера кода участников: %s" % team1_num, "!")

team2_num = 6
print("Итого сегодня в командах участников: %s и %s!" % (team1_num, team2_num))

team2_solve = 42
print("Команда Волшебники данных решила задач: {}!".format(team2_solve))

team1_time = 18015.2
print("Волшебники данных решили задачи за 18015.2 с !".format(team1_time))
team2_time = 2153.31451

score_1 = 40
score_2 = 42
print(f'Команды решили {score_1} и {score_2} задач.')

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'Победа команды Волшебники Данных!'
else:
    challenge_result = 'Ничья!'
print(f'Результат битвы: победа команды {challenge_result}')

tasks_total = score_1+score_2
time_avg = (team1_time+team2_time)/tasks_total
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')

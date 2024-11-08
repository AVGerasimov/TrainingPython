__author__ = 'Андрей Герасимов'

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age


class Video:
    def __init__(self, title, duration,  adult_mode):
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode
        time_now = 0
        bool = False

class UrTube:

    def __init__(self):
        self.users = []
        videos = []


    def register (self, nickname, password, age):
        if len(self.users)==0:# если не было ни одного пользователя в списке, добавляем сразу
            x = User(nickname, password, age)
            self.users.append(x)


        for i in self.users:
            if (i.nickname != nickname and i.password != password and i.age != age):
                x = User(nickname, password, age)
                self.users.append(x)
                break


    def log_in(self,nickname, password ):
        for i in self.users:
            if i.nickname == nickname and i.password == password:
                current_user = i
                print("Есть такой пользователь!")


ur = UrTube()
ur.register('Oleg','kolbasa', 35)
ur.register('Sanya','kolbasa2', 26)
ur.register('Nik','kolbasa21', 41)
for i in ur.users:
    print(i.nickname)
ur.log_in('Oleg','kolbasa')



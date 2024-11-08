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
    users = [User]
    videos = [Video]

    def __init__(self):
        pass


    def log_in(self,nickname, password ):
        for i in self.users:
            if i.nickname == nickname and i.password == password:
                current_user = i
                print("OK")

    def register (self, nickname, password, age):
        for i in self.users:
            if (i.nickname != nickname and i.password != password and i.age != age):
                x = User(nickname, password, age)
                self.users.append(x)



ur = UrTube()
#ur.log_in('Oleg','kolbasa')
#ur.register('Oleg','kolbasa', 35)



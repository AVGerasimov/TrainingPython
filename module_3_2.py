__author__ = 'Андрей Герасимов'

def send_email ( message, recipient, sender = "university.help@gmail.com"):

    Correct_recipient = False
    if  ("@" in recipient) and ((recipient[-3:] == ".ru") or (recipient[-4:] == ".com") or (recipient[-4:] == ".net")) \
            and ("@" in sender) and ((sender[-3:] == ".ru") or (sender[-4:] == ".com") or (sender[-4:] == ".net"))                                                                                                              :
        Correct_recipient = True
    if Correct_recipient == False:
        print("Невозможно отправить письмо с адреса ", sender, " на адрес ", recipient, ".")
    if recipient == sender:
        print('Нельзя отправить письмо самому себе!')
        Correct_recipient = False

    if (Correct_recipient == True) and (sender == "university.help@gmail.com"):
        print("Письмо успешно отправлено с адреса ", sender ," на адрес ", recipient, ".")

    if (Correct_recipient == True) and (sender != "university.help@gmail.com"):
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса ", sender, " на адрес ", recipient, ".")



send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
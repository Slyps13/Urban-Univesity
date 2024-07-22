def send_email(message,recipient,*, sender = 'university.help@gmail.com') :
  corect_R = ('@' in recipient)and(('.com'  in recipient)or('.ru'  in recipient)or('.net'  in recipient))
  corect_S = ('@' in sender)and(('.com'  in sender)or('.ru'  in sender)or('.net'  in sender))
  if  corect_R and corect_S :
    if recipient == sender :
     print('Нельзя отправить письмо самому себе!')  
     return
    if not (sender == 'university.help@gmail.com') :
       print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса ' + sender + ' на адрес ' + recipient)
       return
    print('Письмо успешно отправлено с адреса ' + sender + ' на адрес ' + recipient)  
  else :
    print('Невозможно отправить письмо с адреса  ' + sender + ' на адрес ' + recipient)
    return

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')

send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
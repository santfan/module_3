# Объявим принимающую функцию
def send_email(message, recipient, sender = 'university.help@gmail.com'):
  # Проверим выполняется ли тебования к эл. адресу
  if ((recipient[recipient.rfind('.'):] in ['.com', '.ru', '.net']) +
      ('@' in recipient) + ('@' in sender) +
      (sender[sender.rfind('.'):] in ['.com', '.ru', '.net'])) != 4:
      print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')
  # Проверим совпадения адресов получателя и отправителя
  elif sender == recipient:
      print('Нельзя отправить письмо самому себе!')
  # Проверим условие нестандартного адреса отправителя
  elif sender != 'university.help@gmail.com':
      print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')
  # В противном случае
  else:
      print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')

# Проведем тестовые отправления
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')

send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')

send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')

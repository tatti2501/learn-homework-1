"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например: 
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user_dict() которая с помощью input() просит 
  пользователя ввести вопрос, а затем, если вопрос есть в словаре, 
  программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""
glossary={"Как дела?": "Хорошо!", "Что делаешь?": "Программирую", "А что нужно делать?":"Исправлять ошибки в слайдах"}
def ask_user(wert):
    
    while True:
        user_say=input('Спроси что-нибудь ')
        if user_say in wert:
            print(wert[user_say])
        elif user_say=="Пока":
            print("Пока, пока!")
            break
        else:
            print('Сам ты {}'.format(user_say))
            


if __name__ == "__main__":
    ask_user(glossary)
# while True:
#         user_say= input('Как дела? ')
#         if user_say=='Хорошо':
#             print('И у меня отлично! ')
#             break
#         else:
#             print('А еще? ')
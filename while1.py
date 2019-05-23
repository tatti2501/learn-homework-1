"""

Домашнее задание №1

Цикл while: ask_user

* Напишите функцию ask_user(), которая с помощью input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def ask_user():
    while True:
        user_say= input('Как дела? ')
        if user_say=='Хорошо':
            print('И у меня отлично! ')
            break
        else:
            print('А еще? ')

    
if __name__ == "__main__":
    ask_user()

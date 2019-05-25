"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""
glossary={"Как дела?": "Хорошо!", "Что делаешь?": "Программирую", "А что нужно делать?":"Исправлять ошибки в слайдах"}

def ask_user(wert):
    while True:
        try:
            user_say = input('Спроси что-нибудь ')
        except KeyboardInterrupt:
            print('Пока!')
            break
        if user_say in wert:
            print(wert[user_say])
        elif user_say == "Пока":
            print("Пока, пока!")
            break
            
if __name__ == "__main__":
    ask_user(glossary)

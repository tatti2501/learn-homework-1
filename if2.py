# """

# Домашнее задание №1

# Условный оператор: Сравнение строк

# * Написать функцию, которая принимает на вход две строки
# * Проверить, является ли то, что передано функции, строками. 
#   Если нет - вернуть 0
# * Если строки одинаковые, вернуть 1
# * Если строки разные и первая длиннее, вернуть 2
# * Если строки разные и вторая строка 'learn', возвращает 3
# * Вызвать функцию несколько раз, передавая ей разные праметры 
#   и выводя на экран результаты

# """

# def main():
#     """
#     Эта функция вызывается автоматически при запуске скрипта в консоли
#     В ней надо заменить pass на ваш код
#     """
#     pass
    
# if __name__ == "__main__":
#     main()

text1=input('Напишите что-нибудь ')
text2=input('И еще что-нибудь ')


def main(text1, text2):
    
    if text1==text2:
        return(1)
    elif text1!=text2:
        if len(text1)>len(text2):
            return(2)
    elif text1!=text2:
        if text2=='learn':
            return(3)
    
    text1=isinstance(text1, str)
    text2=isinstance(text2, str)
    if text1 == True:
        if text2 == True:
            return (0)
        

name=main(text1, text2)
print(name)

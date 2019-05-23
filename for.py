# """

# Домашнее задание №1

# Цикл for: Оценки

# * Создать список из словарей с оценками учеников разных классов 
#   школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
# * Посчитать и вывести средний балл по всей школе.
# * Посчитать и вывести средний балл по каждому классу.
# """

# def main():
#     """
#     Эта функция вызывается автоматически при запуске скрипта в консоли
#     В ней надо заменить pass на ваш код
#     """
#     pass
    
# if __name__ == "__main__":
#     main()

line=('привет мир!')
for number in line:
    print(number)

journal=[{'school_class': '4a', 'scores': [3,4,4,5,2]}, {'school_class': '5b', 'scores': [5,3,4,5,2]},{'school_class': '6c', 'scores': [2,5,5,4,3]}]

journal[0]['scores']=sum(journal[0]['scores'])/len(journal[0]['scores'])

for grade_for_class in journal:
        print(grade_for_class)

def sum(scores, start):
    return start
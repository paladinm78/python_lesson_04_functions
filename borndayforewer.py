"""
МОДУЛЬ 2
Программа из 2-го дз
Сначала пользователь вводит год рождения Пушкина, когда отвечает верно вводит день рождения
Можно использовать свой вариант программы из предыдущего дз, мой вариант реализован ниже
Задание: переписать код используя как минимум 1 функцию
"""


def ask_while_not_true(question, correct_answer):
    answer = None
    while answer != correct_answer:
        print("Не верно")
        answer = input(question)


ask_while_not_true('Введите год рождения А.С.Пушкина: ', '1799')
ask_while_not_true('Введите день рождения А.С.Пушкина: ', '6')
print('Верно')

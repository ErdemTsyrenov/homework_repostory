"""
В этом задании будем улучшать нашу систему классов из задания прошлой лекции
(Student, Teacher, Homework)
Советую обратить внимание на defaultdict из модуля collection для
использования как общую переменную
1. Как то не правильно, что после do_homework мы возвращаем все тот же
объект - будем возвращать какой-то результат работы (HomeworkResult)
HomeworkResult принимает объект автора задания, принимает исходное задание
и его решение в виде строки
Атрибуты:
    homework - для объекта Homework, если передан не этот класс -  выкинуть
    подходящие по смыслу исключение с сообщением:
    'You gave a not Homework object'
    solution - хранит решение ДЗ как строку
    author - хранит объект Student
    created - c точной датой и временем создания
2. Если задание уже просрочено хотелось бы видеть исключение при do_homework,
а не просто принт 'You are late'.
Поднимайте исключение DeadlineError с сообщением 'You are late' вместо print.
3. Student и Teacher имеют одинаковые по смыслу атрибуты
(last_name, first_name) - избавиться от дублирования с помощью наследования
4.
Teacher
Атрибут:
    homework_done - структура с интерфейсом как в словаря, сюда поподают все
    HomeworkResult после успешного прохождения check_homework
    (нужно гаранитровать остутствие повторяющихся результатов по каждому
    заданию), группировать по экземплярам Homework.
    Общий для всех учителей. Вариант ипользования смотри в блоке if __main__...
Методы:
    check_homework - принимает экземпляр HomeworkResult и возвращает True если
    ответ студента больше 5 символов, так же при успешной проверке добавить в
    homework_done.
    Если меньше 5 символов - никуда не добавлять и вернуть False.
    reset_results - если передать экземпряр Homework - удаляет только
    результаты этого задания из homework_done, если ничего не передавать,
    то полностью обнулит homework_done.
PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
import datetime
from collections import defaultdict


class DeadlineError(Exception):
    pass


class Homework:
    def __init__(self, text: str, days_to_complete: int):
        self.text = text
        self.deadline = datetime.timedelta(days=days_to_complete)
        self.created = datetime.datetime.now()

    def is_active(self) -> bool:
        return self.created + self.deadline > datetime.datetime.now()

    def __hash__(self):
        return hash((self.text, self.deadline, self.created))


class Person:
    def __init__(self, last_name: str, first_name: str):
        self.last_name = last_name
        self.first_name = first_name

    def __hash__(self):
        return hash((self.last_name, self.first_name))


class HomeworkResult:
    def __init__(self, author, homework: Homework, solution: str):
        if not isinstance(homework, Homework):
            raise ValueError('You gave not a Homework object')
        self.author = author
        self.homework = homework
        self.solution = solution
        self.created = datetime.datetime.now()

    def __hash__(self):
        return hash((self.author, self.homework, self.solution, self.created))


class Student(Person):
    def do_homework(self, homework: Homework, solution: str) -> HomeworkResult:
        if homework.is_active():
            return HomeworkResult(self, homework, solution)
        else:
            raise DeadlineError('You are late')


class Teacher(Person):
    homework_done = defaultdict(set)

    @staticmethod
    def create_homework(text: str, days_to_complete: int) -> Homework:
        return Homework(text, days_to_complete)

    @staticmethod
    def check_homework(hw_result: HomeworkResult) -> bool:
        if len(hw_result.solution) >= 5:
            Teacher.homework_done[hw_result.homework].add(hw_result)
            return True
        else:
            return False

    @staticmethod
    def reset_results(homework: Homework = None):
        if homework is None:
            Teacher.homework_done.clear()
        else:
            Teacher.homework_done[homework].clear()

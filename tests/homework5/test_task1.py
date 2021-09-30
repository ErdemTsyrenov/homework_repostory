import pytest

from homework5.task1 import Student, Teacher


def test_homework():
    teacher = Teacher('Daniil', 'Shadrin')
    expired_homework = teacher.create_homework('Learn functions', 0)
    expired_homework.created  # Example: 2019-05-26 16:44:30.688762
    expired_homework.deadline  # 0:00:00
    expired_homework.text  # 'Learn functions'
    student = Student('Roman', 'Petrov')
    assert student.do_homework(expired_homework) is None


@pytest.mark.parametrize('first_name, last_name', [('Daniil', 'Shadrin')])
def test_teacher(first_name, last_name):
    teacher = Teacher(last_name, first_name)
    assert teacher.first_name == first_name
    assert teacher.last_name == last_name


@pytest.mark.parametrize('first_name, last_name', [('Daniil', 'Shadrin')])
def test_student(first_name, last_name):
    student = Student(last_name, first_name)
    assert student.first_name == first_name
    assert student.last_name == last_name

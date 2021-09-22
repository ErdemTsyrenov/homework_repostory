import pytest

from homework6.task2 import (DeadlineError, Homework, HomeworkResult, Student,
                             Teacher)


def test_homework_result():
    hw = Homework('This is homework', 2)
    student = Student('Jerome', 'Jerome')
    HomeworkResult(student, hw, 'this is good solution')
    try:
        HomeworkResult(student, 'wrong hw format', 'this is good solution')
    except ValueError:
        pass


@pytest.mark.parametrize('last_name, first_name', [('Potter', 'Harry')])
def test_student_teacher_inheritance_from_person(last_name, first_name):
    st = Student(last_name, first_name)
    assert st.last_name == last_name
    assert st.first_name == first_name
    tchr = Teacher(last_name, first_name)
    assert tchr.last_name == last_name
    assert tchr.first_name == first_name


def test_student_do_homework():
    active_hw = Homework('This is homework', 2)
    student = Student('Jerome', 'Jerome')
    hw_res = student.do_homework(active_hw, 'hw solution')
    assert hw_res.homework == active_hw
    assert hw_res.author == student
    assert hw_res.solution == 'hw solution'
    inactive_hw = Homework('This is inactive hw', 0)
    try:
        student.do_homework(inactive_hw, 'hw solution')
    except DeadlineError:
        pass


def test_teacher_check_homework():
    opp_teacher = Teacher('Daniil', 'Shadrin')
    advanced_python_teacher = Teacher('Aleksandr', 'Smetanin')

    lazy_student = Student('Roman', 'Petrov')
    good_student = Student('Lev', 'Sokolov')

    oop_hw = opp_teacher.create_homework('Learn OOP', 1)
    docs_hw = opp_teacher.create_homework('Read docs', 5)

    result_1 = good_student.do_homework(oop_hw, 'I have done this hw')
    result_2 = good_student.do_homework(docs_hw, 'I have done this hw too')
    result_3 = lazy_student.do_homework(docs_hw, 'done')

    opp_teacher.check_homework(result_1)
    temp_1 = opp_teacher.homework_done
    advanced_python_teacher.check_homework(result_1)
    temp_2 = Teacher.homework_done
    assert temp_1 == temp_2

    opp_teacher.check_homework(result_2)
    opp_teacher.check_homework(result_3)
    assert opp_teacher.homework_done == Teacher.homework_done
    assert len(Teacher.homework_done) == 2
    assert len(Teacher.homework_done[docs_hw]) == 1


def test_teacher_reset_homework():
    opp_teacher = Teacher('Daniil', 'Shadrin')
    advanced_python_teacher = Teacher('Aleksandr', 'Smetanin')

    lazy_student = Student('Roman', 'Petrov')
    good_student = Student('Lev', 'Sokolov')

    oop_hw = opp_teacher.create_homework('Learn OOP', 1)
    docs_hw = opp_teacher.create_homework('Read docs', 5)

    result_1 = good_student.do_homework(oop_hw, 'I have done this hw')
    result_2 = good_student.do_homework(docs_hw, 'I have done this hw too')
    result_3 = lazy_student.do_homework(docs_hw, 'done')

    opp_teacher.check_homework(result_1)
    advanced_python_teacher.check_homework(result_1)
    opp_teacher.check_homework(result_2)
    opp_teacher.check_homework(result_3)

    opp_teacher.reset_results(oop_hw)
    assert len(Teacher.homework_done[oop_hw]) == 0
    advanced_python_teacher.reset_results()
    assert len(Teacher.homework_done) == 0

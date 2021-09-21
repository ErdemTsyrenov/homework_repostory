"""
Написать декоратор который позволит сохранять информацию из
исходной функции (__name__ and __doc__), а так же сохранит саму
исходную функцию в атрибуте __original_func
print_result изменять нельзя, за исключением добавления вашего
декоратора на строку отведенную под него - замените комментарий
До применения вашего декоратор будет вызываться AttributeError
при custom_sum.__original_func
Это корректное поведение
После применения там должна быть исходная функция
Ожидаемый результат:
print(custom_sum.__doc__)
# 'This function can sum any objects which have __add___'
print(custom_sum.__name__)  # 'custom_sum'
print(custom_sum.__original_func)  # <function custom_sum at <some_id>>
"""

from typing import Callable


class FuncInfo:
    def __init__(self, __name__, __doc__, __original_func__, wrapped):
        self.__original_func__ = __original_func__
        self.__name__ = __name__
        self.__doc__ = __doc__
        self.wrapped = wrapped

    def __call__(self, *args, **kwargs):
        return self.wrapped(*args, **kwargs)


def save_func_data(func: Callable, func_to_save: Callable = None):
    func_info = FuncInfo(func_to_save.__name__, func_to_save.__doc__,
                         func_to_save, func)
    return func_info


def print_result(func):
    # Place for new decorator
    def save_func():
        def wrapper(*args, **kwargs):
            """Function-wrapper which print result of an original function"""
            result = func(*args, **kwargs)
            print(result)
            return result
        func_info = FuncInfo(func.__name__, func.__doc__, func, wrapper)
        return func_info
    return save_func()

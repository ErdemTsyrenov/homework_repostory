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


def save_func(func_to_save):
    def wrapper(func_to_wrap):
        func_to_wrap.__doc__ = func_to_save.__doc__
        func_to_wrap.__name__ = func_to_save.__name__
        setattr(func_to_wrap, '__original_func__', func_to_save)
        return func_to_wrap
    return wrapper


def print_result(func):
    # Place for new decorator
    @save_func(func)
    def wrapper(*args, **kwargs):
        """Function-wrapper which print result of an original function"""
        result = func(*args, **kwargs)
        print(result)
        return result
    return wrapper

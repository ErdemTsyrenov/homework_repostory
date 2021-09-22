"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять
Ниже пример использования
"""


def instances_counter(cls):
    """Some code"""
    class Counter(cls):
        created_instances = 0

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            Counter.created_instances += 1

        @staticmethod
        def get_created_instances():
            return Counter.created_instances

        @staticmethod
        def reset_instances_counter():
            old_value = Counter.created_instances
            Counter.created_instances = 0
            return old_value
    cls = Counter
    return cls

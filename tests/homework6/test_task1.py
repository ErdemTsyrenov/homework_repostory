import pytest

from homework6.task1 import instances_counter


@instances_counter
class User:
    def __init__(self, name):
        self.name = name
        print(f'User {self.name} created')

    def login(self):
        print(f'User {self.name} login')


@pytest.mark.parametrize('expected', [0, 2, 4])
def test_get_created_instances(expected):
    [User('Name') for i in range(expected)]
    assert User.get_created_instances() == expected
    User.reset_instances_counter()


@pytest.mark.parametrize('expected', [0, 2, 4])
def test_reset_instances_counter(expected):
    [User('Name') for i in range(expected)]
    assert User.reset_instances_counter() == expected
    assert User.reset_instances_counter() == 0

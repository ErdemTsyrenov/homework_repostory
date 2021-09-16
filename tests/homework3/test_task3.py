import pytest

from homework3.task3 import make_filter

sample_data = [
    {
        "name": "Bill",
        "last_name": "Gilbert",
        "occupation": "was here",
        "type": "person",
    },
    {
        "is_dead": True,
        "kind": "parrot",
        "type": "bird",
        "name": "polly"
    }
]


@pytest.mark.parametrize('keys, answer', [
        ({'name': 'Bill', 'type': 'person'}, [sample_data[0]]),
        ({'kind': 'parrot', 'type': 'bird'}, [sample_data[1]])
])
def test_exist_keys(keys, answer):
    assert make_filter(**keys).apply(sample_data) == answer


@pytest.mark.parametrize('keys, answer', [
        ({'last_name': 'Gilbert', 'type': 'dog'}, []),
        ({'type': 'bird', 'occupation': 'was here'}, []),
        ({'last_name': 'Gilbert', 'type': 'bird'}, []),
        ({'type': 'bird', 'home': 'was here'}, []),
])
def test_non_exist_keys(keys, answer):
    assert make_filter(**keys).apply(sample_data) == answer

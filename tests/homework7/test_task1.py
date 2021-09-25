import pytest

import homework7.task1 as task

example_tree1 = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        }
     },
    "fourth": "RED",
}


example_tree2 = example_tree1.copy()
example_tree2["fifth"] = example_tree1


@pytest.mark.parametrize('test_data, element, expected',
                         [(example_tree1, 'RED', 6),
                          (example_tree1, 'BLUE', 2),
                          (example_tree1, 'NotExist', 0)])
def test_simple_tree(test_data, element, expected):
    assert task.find_occurrences(test_data, element) == expected


@pytest.mark.parametrize('test_data, element, expected',
                         [(example_tree2, 'RED', 12),
                          (example_tree2, 'BLUE', 4),
                          (example_tree2, 'NotExist', 0)])
def test_big_tree(test_data, element, expected):
    assert task.find_occurrences(test_data, element) == expected

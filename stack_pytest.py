import balans
from balans import Stack, stack, str_stack
import pytest
from parameterized import parameterized

fixture = [
    ("(((([{}]))))", True),
    ("", True),
    ("{{[(])]}}", False)
]


@pytest.mark.parametrize("str_stack, result", fixture)
def test_balans( str_stack, result):
    s = Stack()
    test_result = s.balans(str_stack)
    assert test_result == result

if __name__ == '__main__':
    test_balans(str_stack)
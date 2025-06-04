import pytest
from reto1 import longest_substring
from reto2 import is_authentic_skewer

# Tests for longest_substring based on README examples
@pytest.mark.parametrize('input_str, expected', [
    ("225424272163254474441338664823", "272163254"),
    ("594127169973391692147228678476", "16921472"),
    ("721449827599186159274227324466", "7214"),
])
def test_longest_substring_examples(input_str, expected):
    assert longest_substring(input_str) == expected

# Tests for is_authentic_skewer based on README examples
@pytest.mark.parametrize('skewer, expected', [
    ("B--A--N--A--N--A--S", True),
    ("A--X--E", False),
    ("C-L-A-P", False),
    ("M--A---T-E-S", False),
])
def test_is_authentic_skewer_examples(skewer, expected):
    assert is_authentic_skewer(skewer) is expected

# Additional edge case: empty string should be False
@pytest.mark.parametrize('skewer', ["", "----", "123"])
def test_is_authentic_skewer_invalid(skewer):
    assert not is_authentic_skewer(skewer)

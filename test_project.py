import pytest
from project import navigate_from_main
from project import count_actions
from project import key_print

def main():
    test_count_actions()
    test_navigate_from_main()
    test_key_print()


def test_navigate_from_main():
    with pytest.raises(SystemExit):
        navigate_from_main("3")

def test_count_actions():
    dict = {"1":"4",
            "2":"3",
            "3":"2",
            "4":"1",}
    assert count_actions(dict) == ["1","2","3","4"]

def test_key_print():
    assert key_print() == print("\nPress the key to take an action\n")
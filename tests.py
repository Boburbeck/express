import pytest
from express_test_task import linked_list
from express_test_task import convert_to_single_digit
from express_test_task import convert_to_list_of_integers


def test_data_type():
    arg_1 = 1
    arg_2 = 5
    with pytest.raises(ValueError):
        linked_list(arg_1, arg_2)


def test_valid_functionality():
    list_a = [1, 2]
    list_b = [9, 8]
    assert linked_list(list_a, list_b) == [0, 1, 1]

    list_a = [5, 9, 6, 6, 3]
    list_b = [9, 8]
    assert linked_list(list_a, list_b) == [1, 6, 7, 9, 5]

    list_a = [9, 9, 9, 9, 9, 9, 9]
    list_b = [9, 9, 9, 9]
    assert linked_list(list_a, list_b) == [8, 9, 9, 9, 0, 0, 0, 1]


def test_convert_to_single_digit():
    dummy_list = [9, 9, 9, 9, 9, 9, 9]
    assert convert_to_single_digit(dummy_list) == 9999999

    dummy_list = [1, 2, 3, 4, 5]
    assert convert_to_single_digit(dummy_list) == 12345


def test_convert_to_list_of_integers():
    dummy_number = 9999999
    assert convert_to_list_of_integers(dummy_number) == [9, 9, 9, 9, 9, 9, 9]

    dummy_number = 12345
    assert convert_to_list_of_integers(dummy_number) == [1, 2, 3, 4, 5]

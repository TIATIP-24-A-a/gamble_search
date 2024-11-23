import pytest
from src.gamble_search import gamble_search

@pytest.fixture
def small_array():
    return ["apple", "banana", "cherry"]

@pytest.fixture
def medium_array():
    return [f"item_{i}" for i in range(100)]

@pytest.fixture
def large_array():
    return [f"item_{i}" for i in range(1000000)]

def test_gamble_search_should_return_correct_answer_with_small_sample(small_array):
    assert gamble_search(small_array, "cherry") == 2

def test_gamble_search_should_return_correct_answer_with_medium_sample(medium_array):
    assert gamble_search(medium_array, "item_50") == 50

def test_gamble_search_should_return_correct_answer_with_large_sample(large_array):
    assert gamble_search(large_array, "item_785302") == 785302

def test_gamble_search_should_raise_type_error_if_array_is_not_string_array():
    invalid_arrays = [
        [1, "two", "three"],
        [3.14, "two", "three"],
        [None, "two", "three"],
        [{}, "two", "three"],
        [[], "two", "three"]
    ]

    for invalid_array in invalid_arrays:
        with pytest.raises(ValueError):
            gamble_search(invalid_array, "three")

def test_gamble_search_should_return_none_if_target_not_found(large_array):
    assert gamble_search(large_array, "cherry") is None

def test_gamble_should_return_value_error_if_target_not_a_string(large_array):
    invalid_targets = [
        True,
        None,
        1,
        2.45,
        [],
        {}
    ]

    for invalid_target in invalid_targets:
        with pytest.raises(TypeError):
            gamble_search(large_array, invalid_target)

def test_gamble_should_return_type_error_if_array_is_not_an_array():
    invalid_arrays = [
        True,
        None,
        1,
        2.45
    ]

    for invalid_array in invalid_arrays:
        with pytest.raises(TypeError):
            gamble_search(invalid_array, "cherry")

def test_gamble_should_return_none_if_array_is_empty():
    assert gamble_search([], "cherry") is None

def test_gamble_should_ignore_case_of_target_and_array(small_array):
    assert gamble_search(small_array, "ChErRy") == 2

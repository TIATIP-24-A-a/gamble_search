import random

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

def test_gamble_search_should_return_value_error_if_small_array_is_unsorted(small_array):
    unsorted = small_array.copy()
    unsorted[0], unsorted[-1] = unsorted[-1], unsorted[0]

    with pytest.raises(ValueError):
        gamble_search(unsorted, "cherry")

def test_gamble_search_should_return_value_error_if_medium_array_is_unsorted(medium_array):
    unsorted = medium_array.copy()
    # Pick a random index (but not 0) from the array
    random_index = random.randint(1, len(unsorted) - 1)
    unsorted[0], unsorted[random_index] = unsorted[random_index], unsorted[0]

    with pytest.raises(ValueError):
        gamble_search(unsorted, "item_1")

def test_gamble_search_should_return_value_error_if_large_array_is_unsorted(large_array):
    unsorted = large_array.copy()
    # Pick two different random indices from the array
    index1, index2 = random.sample(range(len(unsorted)), 2)
    # Swap them
    unsorted[index1], unsorted[index2] = unsorted[index2], unsorted[index1]

    with pytest.raises(ValueError):
        gamble_search(unsorted, "item_1")

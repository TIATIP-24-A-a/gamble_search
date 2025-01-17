import pytest
from src.gamble_search import gamble_search

@pytest.fixture
def small_array():
    return ["apple", "banana", "cherry"]

@pytest.fixture
def medium_array():
    max_value = 99
    num_digits = len(str(max_value))
    return [f"item_{i:0{num_digits}d}" for i in range(100)]

@pytest.fixture
def large_array():
    max_value = 9999
    num_digits = len(str(max_value))
    return [f"item_{i:0{num_digits}d}" for i in range(10000)]

@pytest.fixture
def very_large_array():
    max_value = 999999
    num_digits = len(str(max_value))
    return [f"item_{i:0{num_digits}d}" for i in range(1000000)]

def create_test_array(size: int) -> list[str]:
    num_digits = len(str(size))
    return [f"item_{i:0{num_digits}d}" for i in range(size)]

@pytest.mark.benchmark(
    group="gamble-search",
    min_rounds=10000,
    warmup=True
)
class TestGambleSearchPerformance:

    @pytest.mark.parametrize("size", [
        10,
        100,
        1000,
        10000,
        100000,
        1000000
    ])
    def test_array_performance(self, benchmark, size):
        array = create_test_array(size)
        num_digits = len(str(size))
        target = f"item_{(size // 2):0{num_digits}d}"

        def run_search():
            return gamble_search(array, target)

        result = benchmark(run_search)
        assert result is not None

    def test_found_item_performance(self, benchmark, medium_array):

        def run_search():
            return gamble_search(medium_array, "item_50")

        result = benchmark(run_search)
        assert result is not None

    def test_missing_item_performance(self, benchmark, medium_array):

        def run_search():
            return gamble_search(medium_array, "nonexistent")

        result = benchmark(run_search)
        assert result is None

def test_gamble_search_should_return_correct_answer_with_small_sample(small_array):
    assert gamble_search(small_array, "cherry") == 2

def test_gamble_search_should_return_correct_answer_with_medium_sample(medium_array):
    assert gamble_search(medium_array, "item_50") == 50

def test_gamble_search_should_return_correct_answer_with_very_large_sample(very_large_array):
    assert gamble_search(very_large_array, "item_785302") == 785302

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

def test_gamble_search_should_return_none_if_target_not_found(very_large_array):
    assert gamble_search(very_large_array, "cherry") is None

def test_gamble_should_return_value_error_if_target_not_a_string(very_large_array):
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
            gamble_search(very_large_array, invalid_target)

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

def test_gamble_should_return_none_if_target_empty_string(very_large_array):
    assert gamble_search(very_large_array, "") == None

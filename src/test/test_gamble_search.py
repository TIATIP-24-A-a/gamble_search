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
    return [f"item_{i}" for i in range(10000)]
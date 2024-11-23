import random

def gamble_search(array: list[str], target: str) -> int:
    left, right = 0, len(array) - 1

    while left <= right:
        pivot = random.randint(left, right)
        if array[pivot] == target:
            return pivot
        elif array[pivot] < target:
            left = pivot + 1
        else:
            right = pivot - 1

    return 0

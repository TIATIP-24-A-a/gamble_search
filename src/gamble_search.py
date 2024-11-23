import random

def gamble_search(array: list[str], target: str) -> int | None:
    if not isinstance(array, list):
        raise TypeError("array must be of type list")
    if not all(isinstance(item, str) for item in array):
        raise ValueError("array must be a list of strings")
    if not isinstance(target, str):
        raise TypeError("target must be a string")

    target_lower = target.lower()
    lower_array = [item.lower() for item in array]

    left, right = 0, len(lower_array) - 1

    while left <= right:
        pivot = random.randint(left, right)
        if lower_array[pivot] == target_lower:
            return pivot
        elif lower_array[pivot] < target_lower:
            left = pivot + 1
        else:
            right = pivot - 1

    return None

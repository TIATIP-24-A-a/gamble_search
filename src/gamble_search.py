import random

def gamble_search(array: list[str], target: str) -> int | list[int] | None:
    if not isinstance(array, list):
        raise TypeError("array must be of type list")
    if not all(isinstance(item, str) for item in array):
        raise ValueError("array must be a list of strings")
    if not isinstance(target, str):
        raise TypeError("target must be a string")

    target_lower = target.lower()
    lower_array = [item.lower() for item in array]

    left, right = 0, len(lower_array) - 1
    found_indices = []

    while left <= right:
        pivot = random.randint(left, right)

        if lower_array[pivot] == target_lower:
            found_indices.append(pivot)
            l = pivot - 1
            while l >= 0 and lower_array[l] == target_lower:
                found_indices.append(l)
                l -= 1
            r = pivot + 1
            while r < len(lower_array) and lower_array[r] == target_lower:
                found_indices.append(r)
                r += 1
            break

        elif lower_array[pivot] < target_lower:
            left = pivot + 1
        else:
            right = pivot - 1

    if not found_indices:
        return None
    if len(found_indices) == 1:
        return found_indices[0]
    return sorted(found_indices)

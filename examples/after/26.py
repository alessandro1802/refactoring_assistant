from typing import List

def multiply_list_elements(lst: List[int]) -> int:
    """
    Multiply all elements in the list together.

    Args:
        lst: A list of integers.

    Returns:
        The result of multiplying all elements in the list.
    """
    result = 1
    for num in lst:
        result *= num
    return result

my_list: List[int] = [2, 3, 5, 7]
result: int = multiply_list_elements(my_list)
print(result)

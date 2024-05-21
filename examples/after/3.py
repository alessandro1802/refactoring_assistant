def is_odd_number(num: int) -> bool:
    """
    Check if a number is odd.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if the number is odd, False otherwise.
    """
    if num % 2 != 0:
        return True
    else:
        return False

number: int = 7
if is_odd_number(number):
    print(f'{number} is an odd number.')
else:
    print(f'{number} is not an odd number.')

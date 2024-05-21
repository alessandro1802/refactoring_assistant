def factorial(n: int) -> int:
    """
    Calculates the factorial of a number.

    Args:
        n (int): Input integer.

    Returns:
        int: Factorial of the input number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

result: int = factorial(5)
print(result)

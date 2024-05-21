def add_numbers(a: int, b: int) -> int:
    """
    Adds two numbers and returns the result.
    
    Args:
    a (int): The first number.
    b (int): The second number.
    
    Returns:
    int: The sum of the two numbers.
    """
    result = a + b
    return result

x: int = 5
y: int = 10
output: int = add_numbers(x, y)
print(output)

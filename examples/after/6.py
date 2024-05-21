def greet(name: str) -> str:
    """
    Greets the user with the given name.
    
    Args:
    name (str): The name of the user.
    
    Returns:
    str: A greeting message for the user.
    """
    return f"Hello, {name}!"

user: str = "Alice"
message: str = greet(user)
print(message)

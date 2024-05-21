def calculate_discount(price: float, discount_rate: float) -> float:
    """Calculate discounted price based on the original price and discount rate."""
    discounted_price: float = price - (price * discount_rate)
    return discounted_price

result: float = calculate_discount(100, 0.2)
print(f"Final price after discount: ${result}")

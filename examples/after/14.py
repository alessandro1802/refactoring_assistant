from typing import List

def calculate_total_price(prices: List[float], discounts: List[float]) -> float:
    """
    Calculate the total price after applying discounts.

    Args:
        prices: A list of prices.
        discounts: A list of discount percentages.

    Returns:
        The total price after applying discounts.
    """
    total: float = 0
    for price, discount in zip(prices, discounts):
        total += price - (price * discount / 100)
    return total

prices: List[float] = [100, 200, 300]
discounts: List[float] = [10, 20, 30]
result: float = calculate_total_price(prices, discounts)
print(f"Total price after discounts: {result}")

from typing import List

def calculate_total_price(prices: List[float], tax_rate: float) -> float:
    """
    Calculate the total price including tax.

    Args:
        prices: A list of prices.
        tax_rate: The tax rate in percentage.

    Returns:
        The total price including tax.
    """
    total_price = sum(prices)
    total_price_with_tax = total_price * (1 + tax_rate / 100)
    return total_price_with_tax

items: List[float] = [10, 20, 30]
tax: float = 10

final_price: float = calculate_total_price(items, tax)
print(f"The final price including tax is: {final_price}")

from typing import List

def calculate_total_price(prices: List[float], tax_rate: float) -> float:
    """
    Calculate the total price including tax.

    Args:
        prices: A list of prices.
        tax_rate: The tax rate.

    Returns:
        The total price including tax.
    """
    total = sum(prices)
    total_with_tax = total + total * tax_rate
    return total_with_tax

prices: List[float] = [10.0, 20.0, 30.0]
tax_rate: float = 0.08
final_price: float = calculate_total_price(prices, tax_rate)
print(f"The final price with tax is: {final_price}")

from typing import List

def calculate_total_price(prices: List[float], tax_rate: float) -> float:
    """
    Calculate the total price including tax.

    Args:
        prices: List of prices.
        tax_rate: Tax rate as a decimal value.

    Returns:
        Total price including tax.
    """
    total: float = sum(prices)
    total_with_tax: float = total * (1 + tax_rate)
    return total_with_tax

prices: List[float] = [10, 20, 30]
tax_rate: float = 0.15
final_price: float = calculate_total_price(prices, tax_rate)
print(f"The final price including tax is: {final_price}")

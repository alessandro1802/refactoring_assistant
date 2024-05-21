from typing import List

def calculate_total_cost(prices: List[float], tax_rate: float) -> float:
    """
    Calculate the total cost including tax.

    Args:
        prices: A list of prices for items.
        tax_rate: The tax rate to be applied.

    Returns:
        The total cost including tax.
    """
    total_cost = sum(prices)
    tax_amount = total_cost * tax_rate
    return total_cost + tax_amount

item_prices: List[float] = [10, 20, 30, 40]
tax: float = 0.15
total_cost: float = calculate_total_cost(item_prices, tax)
print(f"The total cost including tax is: {total_cost}")

from typing import List

def calculate_total(items: List[float], tax_rate: float) -> float:
    """Calculate the total cost of items including tax."""
    total = sum(items)
    total_with_tax = total * (1 + tax_rate)
    return total_with_tax

items: List[float] = [10, 20, 30]
tax_rate: float = 0.1
final_total: float = calculate_total(items, tax_rate)
print(final_total)

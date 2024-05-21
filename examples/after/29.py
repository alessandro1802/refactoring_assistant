def calculate_discount(price: float, discount_rate: float) -> float:
    """
    Calculate the final price after applying a discount.

    Args:
        price: The original price.
        discount_rate: The discount rate as a decimal.

    Returns:
        The final discounted price.
    """
    final_price = price - (price * discount_rate)
    return final_price

total_cost: float = 100
discount: float = 0.2
final_cost: float = calculate_discount(total_cost, discount)
print(f'The final cost after applying a {discount*100}% discount is: {final_cost}')

def calculate_discount(price, discount_rate):
    discounted_price = price - (price * discount_rate)
    return discounted_price

result = calculate_discount(100, 0.2)
print(f"Final price after discount: ${result}")

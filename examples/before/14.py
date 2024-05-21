def calculate_total_price(prices, discounts):
    total = 0
    for i in range(len(prices)):
        total += prices[i] - (prices[i] * discounts[i] / 100)
    return total

prices = [100, 200, 300]
discounts = [10, 20, 30]
result = calculate_total_price(prices, discounts)
print(f"Total price after discounts: {result}")

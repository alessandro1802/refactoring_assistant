def calculate_total_price(prices, tax_rate):
    total = sum(prices)
    total_with_tax = total + total * tax_rate
    return total_with_tax

prices = [10, 20, 30]
tax_rate = 0.08
final_price = calculate_total_price(prices, tax_rate)
print(f"The final price with tax is: {final_price}")

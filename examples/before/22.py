def calculate_total_price(prices, tax_rate):
    total = sum(prices)
    total_with_tax = total * (1 + tax_rate)
    return total_with_tax

prices = [10, 20, 30]
tax_rate = 0.15
final_price = calculate_total_price(prices, tax_rate)
print(f"The final price including tax is: {final_price}")

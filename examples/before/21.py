def calculate_total_price(prices, tax_rate):
    total_price = sum(prices)
    total_price_with_tax = total_price * (1 + tax_rate / 100)
    return total_price_with_tax

items = [10, 20, 30]
tax = 10

final_price = calculate_total_price(items, tax)
print(f"The final price including tax is: {final_price}")

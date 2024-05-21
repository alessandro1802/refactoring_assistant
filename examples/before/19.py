def calculate_total_cost(prices, tax_rate):
    total_cost = sum(prices)
    tax_amount = total_cost * tax_rate
    return total_cost + tax_amount

item_prices = [10, 20, 30, 40]
tax = 0.15
total = calculate_total_cost(item_prices, tax)
print(f"The total cost including tax is: {total}")

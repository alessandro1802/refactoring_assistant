def calculate_total(items, tax_rate):
    total = sum(items)
    total_with_tax = total * (1 + tax_rate)
    return total_with_tax

items = [10, 20, 30]
tax_rate = 0.1
final_total = calculate_total(items, tax_rate)
print(final_total)

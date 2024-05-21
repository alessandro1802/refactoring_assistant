def calculate_total_price(items):
    total = 0
    for item in items:
        total += item['price']
    return total

items = [{'name': 'Apple', 'price': 1.50}, {'name': 'Banana', 'price': 0.75}]
result = calculate_total_price(items)
print(f'Total price: ${result}')

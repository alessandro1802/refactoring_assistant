def calculate_total_price(products, discounts):
    total_price = 0
    for product in products:
        price = product['price']
        if product['id'] in discounts:
            price -= discounts[product['id']]
        total_price += price
    return total_price

products = [
    {'id': 1, 'name': 'A', 'price': 10},
    {'id': 2, 'name': 'B', 'price': 20},
    {'id': 3, 'name': 'C', 'price': 15}
]
discounts = {1: 3, 2: 5}

total = calculate_total_price(products, discounts)
print(f"Total price after discounts: ${total}")

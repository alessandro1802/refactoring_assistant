def calculate_total_price(products, prices):
    total_price = 0
    for product in products:
        if product in prices:
            total_price += prices[product]
    return total_price

products = ['apple', 'banana', 'orange']
prices = {'apple': 1.0, 'banana': 0.5, 'grapes': 2.0}

result = calculate_total_price(products, prices)
print(f"Total price: {result}")

def calculate_discount(price, discount_rate):
    final_price = price - (price * discount_rate)
    return final_price

total_cost = 100
discount = 0.2
final_cost = calculate_discount(total_cost, discount)
print(f'The final cost after applying a {discount*100}% discount is: {final_cost}')

def calculate_total(items):
    total = 0
    for item in items:
        total += item
    return total

items_list = [10, 20, 30, 40]
result = calculate_total(items_list)
print("Total:", result)

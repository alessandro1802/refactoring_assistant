def calculate_total(items):
    total = 0
    for item in items:
        total += item
    return total

items = [10, 20, 30]
result = calculate_total(items)
print(f"Total: {result}")

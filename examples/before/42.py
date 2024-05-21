# This function calculates the average of a list of numbers
def calc_average(nums):
    total = sum(nums)
    count = len(nums)
    return total / count

# Example usage
numbers = [5, 10, 15, 20]
result = calc_average(numbers)
print(f"The average is: {result}")

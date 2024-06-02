# Processing data for User A
user_a_data = [1, 2, 3, 4, 5]
user_a_sum = 0
for num in user_a_data:
    user_a_sum += num
user_a_average = user_a_sum / len(user_a_data)
print(f"User A: Sum = {user_a_sum}, Average = {user_a_average}")

# Processing data for User B
user_b_data = [10, 20, 30, 40, 50]
user_b_sum = 0
for num in user_b_data:
    user_b_sum += num
user_b_average = user_b_sum / len(user_b_data)
print(f"User B: Sum = {user_b_sum}, Average = {user_b_average}")

# Processing data for User C
user_c_data = [100, 200, 300, 400, 500]
user_c_sum = 0
for num in user_c_data:
    user_c_sum += num
user_c_average = user_c_sum / len(user_c_data)
print(f"User C: Sum = {user_c_sum}, Average = {user_c_average}")

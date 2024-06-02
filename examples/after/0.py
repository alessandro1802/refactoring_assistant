def process_user_data(user_data, user_name):
    user_sum = sum(user_data)
    user_average = user_sum / len(user_data)
    print(f"{user_name}: Sum = {user_sum}, Average = {user_average}")

# Processing data for User A
user_a_data = [1, 2, 3, 4, 5]
process_user_data(user_a_data, "User A")

# Processing data for User B
user_b_data = [10, 20, 30, 40, 50]
process_user_data(user_b_data, "User B")

# Processing data for User C
user_c_data = [100, 200, 300, 400, 500]
process_user_data(user_c_data, "User C")

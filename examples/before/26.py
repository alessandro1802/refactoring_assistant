def multiply_list_elements(lst):
    res = 1
    for num in lst:
        res *= num
    return res

my_list = [2, 3, 5, 7]
result = multiply_list_elements(my_list)
print(result)

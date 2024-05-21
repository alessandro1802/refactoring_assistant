def is_odd_number(num):
    if num % 2 != 0:
        return True
    else:
        return False

number = 7
if is_odd_number(number):
    print(f'{number} is an odd number.')
else:
    print(f'{number} is not an odd number.')

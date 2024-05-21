# Function to calculate the area of a circle
def calc_area(radius):
    pi = 3.14159
    area = pi * radius * radius
    return area

# Main function to execute the calculation
def main():
    r = 5
    result = calc_area(r)
    print(f"The area of the circle with radius {r} is {result}")

main()

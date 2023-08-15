import random
import string


def coupon_code_odd_sum(coupon_code):
    total_sum = 0
    for i in range(len(coupon_code)):
        if i % 2 == 0:  # Check if the position is odd (1-indexed)
            char = coupon_code[i]
            ascii_value = ord(char)
            if 48 <= ascii_value <= 57:  # ASCII values for digits '0' to '9'
                total_sum += ascii_value - 48  # Convert ASCII digit to its numerical value
            elif 65 <= ascii_value <= 90:  # ASCII values for uppercase letters 'A' to 'Z'
                # Convert ASCII uppercase letter to its numerical value
                total_sum += ascii_value - 64

    return total_sum


def generate_coupon_code(length=10):
    characters = string.ascii_uppercase + string.digits
    coupon_code = ''.join(random.choice(characters) for _ in range(length))

    # Calculate the sum of digits at odd places
    sum_odd_digits = coupon_code_odd_sum(coupon_code)

    # If the sum is not divisible by 10, regenerate the code until it meets the condition
    while sum_odd_digits % 10 != 0:
        coupon_code = ''.join(random.choice(characters) for _ in range(length))
        sum_odd_digits = coupon_code_odd_sum(coupon_code)

    return coupon_code


def is_valid_coupon(coupon_code):
    length = 10  # Length of the coupon code
    valid_characters = string.ascii_uppercase + string.digits

    if len(coupon_code) != length or not all(char in valid_characters for char in coupon_code):
        return False

    # Calculate the sum of digits at odd places
    sum_odd_digits = coupon_code_odd_sum(coupon_code)

    if sum_odd_digits % 10 != 0:
        return False

    return True


while True:
    print("\nMENU:")
    print("1. Generate Coupon Code")
    print("2. Check Coupon Code Validity")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        coupon = generate_coupon_code()
        print("Generated Coupon Code:", coupon)
    elif choice == '2':
        coupon_to_check = input(
            "Enter the coupon code to check validity: ")
        if is_valid_coupon(coupon_to_check):
            print("Coupon is valid!")
        else:
            print("Invalid coupon code.")
    elif choice == '3':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select a valid option.")

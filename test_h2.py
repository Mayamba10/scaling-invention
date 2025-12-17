'''Create a program to check whether the number entered by the user is a disarium number or not using functions.'''

def is_disarium(number):
    num_str = str(number)
    length = len(num_str)
    sum_of_powers = sum(int(digit) ** (index + 1) for index, digit in enumerate(num_str))
    return sum_of_powers == number

def main():
    try:
        user_input = input("Enter a non-negative integer: ").strip()
        number = int(user_input)
        if number < 0:
            print("Please enter a non-negative integer.")
            return
    except ValueError:
        print("Invalid input — please enter an integer.")
        return

    if is_disarium(number):
        print(f"{number} is a Disarium number.")
    else:
        print(f"{number} is not a Disarium number.")
if __name__ == "__main__":
    main()
import time
import math


def safe_input(prompt: str, isNumeric=False, isFloat=False):
    """
    Safely receives user input.
    If isNumeric=True → returns integer.
    If isFloat=True → returns float.
    If both are False → returns lowercase string.
    """

    while True:
        user_input = input(prompt).strip()

        if not user_input:
            print("This field cannot be empty.")
            continue

        # INTEGER MODE
        if isNumeric:
            try:
                return int(user_input)
            except ValueError:
                print("Please enter a valid integer.")
                continue

        # FLOAT MODE
        if isFloat:
            try:
                return float(user_input)
            except ValueError:
                print("Please enter a valid float.")
                continue

        # STRING MODE
        return user_input.lower()


# -------------------- SINGLE OPERATIONS -------------------- #

def absolute_value(n: int):
    print(f"Absolute value of {n} → {abs(n)}")
    quit()


def square_root(n: float):
    if n < 0:
        print("Negative numbers do not have a real square root.")
        print("Converting to positive value...")
        n = abs(n)
        time.sleep(1)

    print(f"Square root of {n} → {math.sqrt(n)}")
    quit()


def power_two(n: float):
    print(f"{n} squared → {n ** 2}")
    quit()


def power_three(n: float):
    print(f"{n} cubed → {n ** 3}")
    quit()


def factorial_value(n: int):
    if n < 0:
        print("Factorial of negative numbers is not defined.")
        print("Converting to positive...")
        n = abs(n)
        time.sleep(1)

    print(f"Factorial of {n} → {math.factorial(n)}")
    quit()


def round_number(n: float):
    print(f"{n} rounded → {round(n)}")
    quit()


def single_operation_mode(operation: int):
    """Handles the single-number operations."""

    if operation == 6:
        value = safe_input("Enter your number: ", isFloat=True)
    else:
        value = safe_input("Enter your number: ", isNumeric=True)

    match operation:
        case 1: absolute_value(value)
        case 2: square_root(value)
        case 3: power_two(value)
        case 4: power_three(value)
        case 5: factorial_value(value)
        case 6: round_number(value)


# -------------------- MULTI OPERATIONS -------------------- #

def map_operator(choice: int):
    match choice:
        case 7: return "+"
        case 8: return "-"
        case 9: return "*"
        case 10: return "/"
        case 11: return "%"
    return None


def multi_operation_mode(operation: int):
    operator = map_operator(operation)
    history = []
    count = 1

    result = safe_input(f"{count}. Enter number: ", isNumeric=True)
    history.append(str(result))

    while True:
        count += 1
        history.append(operator)

        next_value = safe_input(f"{count}. Enter number: ", isNumeric=True)
        history.append(str(next_value))

        match operator:
            case "+":
                result += next_value
            case "-":
                result -= next_value
            case "*":
                result *= next_value
            case "/":
                try:
                    result /= next_value
                except ZeroDivisionError:
                    print("Error: Cannot divide by zero.")
                    history.pop()
                    count -= 1
                    continue
            case "%":
                if count > 3:
                    print("Modulus works only with two numbers.")
                    history.pop()
                    count -= 1
                    continue
                result %= next_value

        # Ask to continue or stop
        choice = safe_input("Continue? (y/n): ", isNumeric=False)

        if choice == "n":
            print("Calculation:")
            print(" ".join(history), "=", result)
            quit()

        operator = safe_input("Select operator (+,-,*,/,%) : ",
                              isNumeric=False, isFloat=False)


# -------------------- MAIN -------------------- #

print("Welcome to the Python Calculator!\n")
time.sleep(1)


def main():

    print("----- SINGLE OPERATIONS -----")
    print("1) Absolute Value")
    print("2) Square Root")
    print("3) Power of Two")
    print("4) Power of Three")
    print("5) Factorial")
    print("6) Round Number\n")

    print("----- MULTI OPERATIONS -----")
    print("7) Addition")
    print("8) Subtraction")
    print("9) Multiplication")
    print("10) Division")
    print("11) Modulus")
    print("-------------------")
    print("12) Exit\n")

    operation = safe_input("Choose your operation: ", isNumeric=True)

    if 1 <= operation <= 6:
        single_operation_mode(operation)
    elif 7 <= operation <= 11:
        multi_operation_mode(operation)
    elif operation == 12:
        print("Thank you for using my program :)")
        quit()
    else:
        print("Invalid operation selected.")


if __name__ == "__main__":
    main()

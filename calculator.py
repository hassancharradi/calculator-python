
"""
Calculator Python
A simple command-line calculator.
"""

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def calculate(a, operator, b):
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }

    if operator not in operations:
        raise ValueError("Unsupported operator.")

    return operations[operator](a, b)


def main():
    print("=== Python Calculator ===")
    print("Available operators: +, -, *, /")
    print("Type 'q' to quit.")

    while True:
        try:
            first = input("\nFirst number: ")

            if first.lower() == "q":
                break

            operator = input("Operator: ")
            second = input("Second number: ")

            result = calculate(
                float(first),
                operator,
                float(second)
            )

            print("Result:", result)

        except ValueError as error:
            print("Error:", error)


if __name__ == "__main__":
    main()

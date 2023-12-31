calculator = """
 _____________________
|  _________________  |
| | 0.              | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
"""
print(calculator)


def add(n1, n2):
    """Add two numbers"""
    return n1 + n2


def subtract(n1, n2):
    """Subtract two numbers"""
    return n1 - n2


def multiply(n1, n2):
    """Multiply two numbers"""
    return n1 * n2


def divide(n1, n2):
    """Divide two numbers"""
    if n2 == 0:
        return "0 divison error"
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator_start():
    num1 = int(input("What is the first number?: "))
    for operator in operations:
        print(operator)
    calculator_on = True

    while calculator_on:
        operation_symbol = input("Pick an operation: ")
        num2 = int(input("What is the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        # Displaying the answer inside the calculator ASCII art
        result_display = f"{answer}"
        calculator_with_answer = calculator.replace("| | 0.              | |", f"| |{result_display.center(17)}| |")
        print(calculator_with_answer)

        continue_calculation = input(
            f"Type 'y' to continue calculating with {answer}, or type 'n' to start again, else type 'quit' to exit: ")

        if continue_calculation == 'y':
            num1 = answer
        elif continue_calculation == 'n':
            calculator_on = False
            calculator_start()
        else:
            quit()


calculator_start()

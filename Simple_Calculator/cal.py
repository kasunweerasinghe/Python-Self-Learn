import os

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# divide
def divide(n1, n2):
    return n1 / n2

# create a dictionary
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# function for calculation
def calculation():
    num1 = float(input("Enter Your first Number: "))

    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Enter Operator: ")
        num2 = float(input("Enter Your second Number: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input("Do you want to continue pres 'y' start over press 'n' ") == 'y':
            num1 = answer
        else:
            should_continue = False
            os.system('clear')
            calculation()


# call the function
calculation()
def multiply(f_number, s_number):
    return f_number * s_number


def add(f_number, s_number):
    return f_number + s_number


def divide(f_number, s_number):
    return f_number / s_number


def subtract(f_number, s_number):
    return f_number - s_number


operations = {
    "*": multiply,
    "+": add,
    "-": subtract,
    "/": divide
}


def execute_operation(f_number, s_number, operator):
    if operator == '+':
        return add(f_number, s_number)

    elif operator == "-":
        return subtract(f_number, s_number)
    elif operator == "/":
        return divide(f_number, s_number)
    elif operator == "*":
        return multiply(f_number, s_number)
    else:
        print("Invalid input")
        return False

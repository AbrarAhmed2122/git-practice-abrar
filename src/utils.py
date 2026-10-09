#def add(a, b):
#    return a + b
#def subtract(a, b):
#    return a - b
#def multiply(a, b):
#    return a * b

#Updated 
def validate_numbers(a, b):
    if not isinstance(a, (int, float)) or isinstance(a, bool):
        raise TypeError("First input must be a number.")

    if not isinstance(b, (int, float)) or isinstance(b, bool):
        raise TypeError("Second input must be a number.")


def add(a, b):
    validate_numbers(a, b)
    return a + b


def subtract(a, b):
    validate_numbers(a, b)
    return a - b


def multiply(a, b):
    validate_numbers(a, b)
    return a * b

def divide(a, b):
    validate_numbers(a, b)

    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")

    return a / b
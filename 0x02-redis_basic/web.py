def execute_operation(operation, a, b):
    return operation(a, b)


# Example of passing a function as a callable argument
def add(x, y):
    return x + y


result = execute_operation(add, 5, 3)
print(result)  # Output will be 8

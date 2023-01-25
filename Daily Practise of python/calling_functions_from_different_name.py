def print_sum(a, b):
    return a + b


print(print_sum(5, 3))


# we can rename a function by creating a new variable an then pass a reference of function to that variable
calculate_sum = print_sum


print(calculate_sum(5, 3))

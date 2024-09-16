def log_decorator(func):
    def print_messages():
        print("Message avant fonction")
        func()
        print("Message après fonction")
    return print_messages

@log_decorator
def function_test():
    print("Cette fonction ne prend pas d'arguments.")

function_test()

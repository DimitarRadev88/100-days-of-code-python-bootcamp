def logging_decorator(function):
    def log_function(*args):
        print(f"You called {function.__name__}{args}")
        result = function(*args)
        print(f"It returned: {result}")
        return result

    return log_function

@logging_decorator
def a_function(*args):
    return sum(args)

a_function(1, 2, 3)
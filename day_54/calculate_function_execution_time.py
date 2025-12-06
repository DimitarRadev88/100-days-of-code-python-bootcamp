import time

print(time.time())


def speed_calculation_decorator(function):
    def execute():
        start = time.time()
        function()
        end = time.time()

        return end - start

    return execute


@speed_calculation_decorator
def fast_function():
    for n in range(1000000):
        n * n


@speed_calculation_decorator
def slow_function():
    for n in range(10000000):
        n * n


print(f"fast_function execution speed{fast_function()}")
print(f"slow_function execution speed{slow_function()}")

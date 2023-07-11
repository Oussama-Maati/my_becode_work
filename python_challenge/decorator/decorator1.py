def decorator(func):
    count = 0

    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1

        if count > 3:
            raise Exception("Function execution limit exceeded")

        return func(*args, **kwargs)

    return wrapper

@decorator
def addition(a, b):
    return a + b

decorator(addition(5,2))
decorator(addition(5,2))
decorator(addition(5,2))
decorator(addition(5,2))
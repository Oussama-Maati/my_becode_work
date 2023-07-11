def decorator(func):
    def wrapper(*args, **kwargs):
        ret = func(*args, **kwargs)
        if type(ret) == int or type(ret) == str:
            raise Exception("The function cannot be string or integers")
        else:
            text = f"Good function return for {func}"
            print(text.replace("<", "").split("at", 1)[0])


        return func(*args, **kwargs)

    return wrapper

@decorator
def addition(a, b):
    return a + b

@decorator
def msg():
    return "Hello Friend"

@decorator
def flo():
    return 5.2

try:
    flo()
except None:
    print("No fail")

try:
    msg()
except Exception:
    "Cant return str with the deco"


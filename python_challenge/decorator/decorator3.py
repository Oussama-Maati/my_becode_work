import re
import sys
import time


def decorator(func):


    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        times = end - start
        text = f"The {func} took {times:.3f} seconds to run"
        pattern = r'at\s+0x[\da-fA-F]+\>'
        text = re.sub(pattern, '', text)
        print(text.replace("<", ""))
        return func(*args, **kwargs)
    return wrapper


@decorator
def addition(a, b):
    time.sleep(3)
    return a + b


addition(5, 2)

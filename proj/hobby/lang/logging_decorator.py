from functools import wraps

def logger(fn):
    @wraps(fn) # Preserves the original function's metadata
    def wrapper(*args, **kwargs):
        print(f"calling {fn.__name__} with {args} and {kwargs}")
        result = fn(*args, **kwargs)
        print(f"{fn.__name__} returned {result}")
        return result
    return wrapper

@logger
def add(x, y):
    return x + y

add(2,4)
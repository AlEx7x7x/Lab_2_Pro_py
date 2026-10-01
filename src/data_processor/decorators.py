from functools import wraps
from time import perf_counter

def measure_time(func):
    """Декоратор для вимірювання часу виконання функції."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        elapsed = perf_counter() - start
        print(f"{func.__name__}: {elapsed:.8f} s")
        return result
    return wrapper

def repeat(count: int):
    """Параметризований декоратор, що повторює виклик функції."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(count):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator
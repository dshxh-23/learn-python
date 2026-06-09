import functools
import time

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} ran in {end-start:.4f} seconds")
        return result
    
    return wrapper

@timer
def slow_sum(n):
    return sum(range(n))

print(slow_sum(10_000_000))
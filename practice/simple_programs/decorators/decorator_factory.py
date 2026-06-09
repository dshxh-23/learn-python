import functools
import time

def retry(times):
    def decorator(func):
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, times+1):
                try:
                    return func(*args, **kwargs)
                except:
                    print(f"attempt {attempt} failed!")
                    time.sleep(0.5)
            raise Exception(f"All {times} attempts failed")
        return wrapper
    return decorator

@retry(times=3)
def fetch_data(url):
    raise ConnectionError("Network down")        

fetch_data("https://example.com")
from datetime import datetime
import logging
from functools import wraps


def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.utcnow()
        result = func(*args, **kwargs)
        end_time = datetime.utcnow()
        logging.info(f"Function {func.__name__} took "
                     f"{round((end_time - start_time).total_seconds(), 3)} seconds to run.")
        return result
    return wrapper


def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Executing {func.__name__} with positional arguments "
                     f"{[arg for arg in args]} and keyword arguments {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"Finished executing {func.__name__}")
        return result
    return wrapper


def log(func):
    def wrapper(*args, **kwargs):
        print(f"Starting {func.__name__} function...")
        result = func(*args, **kwargs)
        print(f"Finished {func.__name__} function.")
        return result
    return wrapper


def cache_decorator(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper


@log
def my_function(x, y):
    return x + y


results = my_function(2, 3)
print(results)

import time
from functools import wraps
import requests

def retry(max_tries=3, delay_seconds=1):
    def decorator_retry(func):
        @wraps(func)
        def wrapper_retry(*args, **kwargs):
            tries = 0
            while tries < max_tries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    tries += 1
                    if tries == max_tries:
                        raise e
                    time.sleep(delay_seconds)
        return wrapper_retry
    return decorator_retry
@retry(max_tries=5, delay_seconds=2)
def call_dummy_api():
    response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    return response


def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time} seconds to run.")
        return result
    return wrapper






'''
Python decorators are excellent way to give new behavior to our functions. It reduces code repetition and help us maintain clean codebase. They are helpful in data science projects in many ways from caching to sending notifications.
Photo by Elena Mozhvilo on Unsplash
At first, every developer’s goal is to get things working. Slowly, we worry about readability and scalability. This is when we first start thinking about decorators.

Decorators are an excellent way to give additional behavior to a function. And there are little things we data scientists often need to inject into a function definition.

With decorators, you’d be surprised to see how much you can reduce code repetition and improve readability. I certainly did.

Create GPT3 Powered Apps in Minutes With Streamlit
Learn to build intelligent apps without worrying too much about software development.
levelup.gitconnected.com

How to Build Simple ETL Pipelines With GitHub Actions
ETLs don’t have to be complex. If that’s the case, use GitHub Actions.
towardsdatascience.com

Here are the five most common ones I use in almost every data-intensive project.

1. The retry decorator
In data science projects and software development projects, there are so many instances where we depend on external systems. Things are not in our control all the time.

3 SQL Optimization Techniques That Can Instantly Boost Query Speed
Simple hacks to try before moving to a different data model altogether
towardsdatascience.com

The Serene Symphony of Python Web Scraping — in 3 Movements
The easiest, the most flexible, and the most comprehensive ways to do web scraping in Python
levelup.gitconnected.com

When an unexpected event occurs, we might want our code to wait a while, allowing the external system to correct itself and rerun.

I prefer to implement this retry logic inside a python decorator so that I can annotate any function to apply the retry behavior.

Here’s the code for a retry decorator.

import time
from functools import wraps
def retry(max_tries=3, delay_seconds=1):
    def decorator_retry(func):
        @wraps(func)
        def wrapper_retry(*args, **kwargs):
            tries = 0
            while tries < max_tries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    tries += 1
                    if tries == max_tries:
                        raise e
                    time.sleep(delay_seconds)
        return wrapper_retry
    return decorator_retry
@retry(max_tries=5, delay_seconds=2)
def call_dummy_api():
    response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    return response
In the above code, we try to get an API response. If it fails, we retry the same task 5 times. Between each retry, we wait for 2 seconds.

2. Caching function results
Some parts of our codebase rarely change their behaviors. Yet, it may take a big chunk of our computation power. In such situations, we can use a decorator to cache function calls.

You Are Not Still Using Virtualenv, Are You?
There is a better way to manage dependencies, package, and publish Python projects.
towardsdatascience.com

The function will run only once if the inputs are the same. In every subsequent run, the results will be pulled from the cache. Hence, we don’t have to perform expensive computations all the time.

def memoize(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            return result
    return wrapper
The decorator uses a dictionary, stores the function args, and returns values. When we execute this function, the decorated will check the dictionary for prior results. The actual function is called only when there’s no stored value before.

The following is a Fibonacci number calculating a function. Since this is a recurrent function, the same function called is performed multiple times. But with caching, we can speed up this process.

@memoize
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
Here are the execution times for this function with and without caching. Note that the cached version only takes a faction of a millisecond to run, whereas the non-cached version almost took a minute.

Function slow_fibonacci took 53.05560088157654 seconds to run.
Function fast_fibonacci took 7.772445678710938e-05 seconds to run.
Using a dictionary to hold previous execution data is a straightforward approach. However, there is a more sophisticated way to store caching data. You can use an in-memory database, such as Redis.

3. Timing functions
This one is no surprise. When working with data-intensive functions, we’re eager to learn how long it takes to run.

The usual way of doing this is by collecting two timestamps, one at the beginning and another at the end of the function. We can then compute the duration and print it along with the return values.

But doing this again and again for multiple functions is a hassle.

Instead, we can have a decorator do it. We can annotate any function that needs a duration printed.

Here’s an example Python decorator that prints the running time of a function when it’s called:

import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time} seconds to run.")
        return result
    return wrapper
You can use this decorator to time the execution of a function:

@timing_decorator
def my_function():
    # some code here
    time.sleep(1)  # simulate some time-consuming operation
    return
Calling the function would print the time it takes to run.

my_function()

>>> Function my_function took 1.0019128322601318 seconds to run.
4. Logging function calls
This one is very much an extension of the previous decorator. But it has some particular uses.

If you follow software design principles, you’d appreciate the single responsibility principle. This essentially means each function will have its one and only one responsibility.

This is How I Create Dazzling Dashboards Purely in Python.
Plotly dash apps are the fastest way to build production-grade dashboards in python.
towardsdatascience.com

When you design your code in such a way, you’d also want to log the execution information of your functions. This is where logging decorators come in handy.

The following example illustrates this.

import logging
import functools

logging.basicConfig(level=logging.INFO)

def log_execution(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Executing {func.__name__}")
        result = func(*args, **kwargs)
        logging.info(f"Finished executing {func.__name__}")
        return result
    return wrapper

@log_execution
def extract_data(source):
    # extract data from source
    data = ...

    return data

@log_execution
def transform_data(data):
    # transform data
    transformed_data = ...

    return transformed_data

@log_execution
def load_data(data, target):
    # load data into target
    ...

def main():
    # extract data
    data = extract_data(source)

    # transform data
    transformed_data = transform_data(data)

    # load data
    load_data(transformed_data, target)
'''

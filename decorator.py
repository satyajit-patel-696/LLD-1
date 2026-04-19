import time
def my_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter() # get the start time
        print(f"start time: {start_time}")
        
        result = func(*args, **kwargs)  # get "hello"
        
        print(result)   # print it in middle
        
        end_time = time.perf_counter()  # get the end time
        print(f"end time: {end_time}")
        print(f"execution time: {end_time - start_time}")

        return result   # still return if needed
    return wrapper


@my_decorator
def say_hello():
    return "hello"


say_hello()




def positive_validation(func):
    def wrapper(args):
        if args<0:
            raise ValueError("Negative value is not allowed")
        return func(args)
    return wrapper
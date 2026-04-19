def retry(max_attempt=3):
    def my_decorator(func):
        def wrapper(*args,**kwargs):
            print("starting")
            for _ in range(max_attempt):
                res=func(*args,**kwargs)
                print(res)
            print("ending")
            return res
        return wrapper
    return my_decorator
@retry(max_attempt=3)
def say_heloo(name:str):
    return f"heloo {name}"
say_heloo("jitu")
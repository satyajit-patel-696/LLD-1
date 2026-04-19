

def presuf(prefix="<<<<",suffix=">>>>>"):
    def my_decorator(func):
        def wrapper(*args):
            print("starting adding")

            res=func(*args)
            print(f"{prefix}{res}{suffix}")
            print("end")
            
            
        return wrapper
    return my_decorator
@presuf("<<<<<",">>>>>")
def my_fun(name="jitu"):
    return name
my_fun()
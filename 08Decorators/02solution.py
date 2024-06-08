def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(f"{k}={v}" for k,v in kwargs.items())
        print(f"calling: {func.__name__} with {args_value} and kwargs {kwargs_value}")
        return func(*args, **kwargs)
    return wrapper
    
@debug
def hello():
    print("Hello")








@debug
def greet(name, greet="Hello"):
    print(f"{greet}, {name}!")

hello()
greet("Hansraj", greet="Namaste")
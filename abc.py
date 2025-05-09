def decorator(func):
    def wrapper():
        print("Executing functions...")
        func()
        print("Function Executed")
    return wrapper()
@decorator
def greet():
    print("Hello, World!")
greet()

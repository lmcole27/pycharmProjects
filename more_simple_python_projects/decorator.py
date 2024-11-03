import time

def decorator_function(function):
    print("outer function")
    def wrapper_function():
        print("inner function")
        time.sleep(2)
        function()
    return wrapper_function()

@decorator_function
def say_hello():
    print("hello")


# say_hello()
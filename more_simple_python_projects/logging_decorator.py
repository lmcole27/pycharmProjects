#Create a logging_decorator() which is going to log the name of the function that was called, 
#the arguments it was given and 
#finally the returned output.
#The expected output is:
#You called a_function(1, 2, 3)
#It returned: 6

def logging_function(function):
    def wrapper(*args, **kwargs):
        print(f"You called {function.__name__}{args}")
        print(f"It returned: {function(args[0], args[1], args[2])}")
    return wrapper

@logging_function
def a_function(n1, n2, n3):
    return (n1*n2*n3)

a_function(1, 2, 3)
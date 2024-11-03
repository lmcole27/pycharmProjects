class User:
    def __init__(self, name):
        self.name = name
        self.logged_in = False


def logged_in_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].login == True:
            function(args[0])
    return wrapper


new_user = User("Linda")
new_user.login = True

@logged_in_decorator
def new_blog_post(user):
    print(f"This is {user.name}'s new blog post!!!")


new_blog_post(new_user)

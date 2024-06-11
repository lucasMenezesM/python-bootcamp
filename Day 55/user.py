class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if kwargs["user"].is_logged_in:
            return function(kwargs["user"])
    return wrapper


@is_authenticated_decorator
def create_blog_post(user):
    print(f"Post created by {user.name}")

lucas = User(name="Lucas")
lucas.is_logged_in = True
create_blog_post(user=lucas)



# def is_authenticated_decorator(function):
#     def wrapper(*args, **kwargs):
#         if args[0].is_logged_in == True:
#             function(args[0])
#     return wrapper
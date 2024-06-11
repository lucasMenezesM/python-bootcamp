import inspect

inputs = eval(input())
# TODO: Create the logging_decorator() function 👇

def loggin_decorator(function):
  def wrapper(*args):
    # params = inspect.signature(function)
    params = (args[0], args[1], args[2])
    result = function(args[0], args[1], args[2])
    print(f"You called {function.__name__}{params}")
    print(f"It returned: {result}")
    return function(args[0], args[1], args[2])
  return wrapper


# TODO: Use the decorator 👇
@loggin_decorator
def a_function(a, b, c):
  return a * b * c

a_function(inputs[0], inputs[1], inputs[2])
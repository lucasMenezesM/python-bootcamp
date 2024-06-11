from flask import Flask
from time import time
from datetime import datetime
from dotenv import load_dotenv

# # load_dotenv()

# app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"   

# if __name__ == "__main__":
#     app.run()


import time
current_time = time.time()
print(current_time) # seconds since Jan 1st, 1970 

# Write your code below 👇

def speed_calc_decorator(function):
    def execute_function():
        current_time = time.time()
        function()
    
    print(time.time() - current_time)
    return execute_function()


@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i
    print("function executed")
        
@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i
    print("function executed")

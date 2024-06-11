from flask import Flask


def bold_decorator(function):
    def return_bold():
        return f"<b>{function()}</b>"
    
    return return_bold


def italic_decorator(function):
    def return_italic():
        return f"<i>{function()}</i>"
    
    return return_italic


def emphasize_decorator(function):
    def return_enphasize():
        return f"<em>{function()}</em>"
    
    return return_enphasize

app = Flask(__name__)

@app.route("/")
@bold_decorator
@italic_decorator
@emphasize_decorator
def hello_world():
    return "<p>Hello, World!</p>"   


if __name__ == "__main__":
    app.run(debug=True)
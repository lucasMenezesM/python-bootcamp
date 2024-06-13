from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("form.html")

user = None
@app.route('/login', methods=['POST'])
def login():
    data = request.form
    user = {"username": data["username"], "password": data["password"]}
    return render_template("form.html", user=user)
    # if user:
    #     print(data["username"])
    #     print(data["password"])
    #     return render_template("index.html", user=user)
    # else:
    #     return

@app.route("/test")
def test():
    data = {
        'name': 'John Doe',
        'age': 30,
        'city': 'New York'
    }

    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
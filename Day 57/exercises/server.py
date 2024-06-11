from flask import Flask, render_template
import random
from datetime import datetime
import requests

now = datetime.now()
current_year = now.year
app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(1, 10)
    return render_template("index.html", random_n=random_number, year=current_year)


@app.route("/guess/<name>")
def guess_page(name):
    response = requests.get(f"https://api.agify.io/?name={name}")
    response.raise_for_status()
    data = response.json()

    age = data["age"]

    response = requests.get(f"https://api.genderize.io/?name={name}")
    response.raise_for_status()
    data = response.json()

    name = data["name"]
    gender = data["gender"]
    count = data["count"]

    print(data)
    print("data type:")
    print(type(data))

    return render_template(
        "guess.html",
        count=count,
        name = name,
        age = age,
        gender = gender
    )


@app.route("/blog")
def blog_home():
    blog_api_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url=blog_api_url)
    data = response.json()

    return render_template("blog.html", posts=data)


if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template
import requests
from post import Post
from functions import get_posts, get_post_by_id

app = Flask(__name__)


@app.route('/')
def home():
    response = requests.get("https://api.npoint.io/c51ff38d4f68ea3a024a")
    response.raise_for_status()
    all_posts = get_posts()

    return render_template("index.html", posts=all_posts)


@app.route("/post/<int:id>")
def post_page(id):
    print(f"id do parametro: {id}")
    post = get_post_by_id(id)
    print(post)
    return render_template("post.html", post=post)



if __name__ == "__main__":
    app.run(debug=True)

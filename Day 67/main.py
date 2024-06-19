from flask import Flask, render_template, redirect, url_for, jsonify, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date
from forms import NewPostForm
from dotenv import dotenv_values
from datetime import datetime

config = dotenv_values("Day 67/.env")
app = Flask(__name__)
app.config['SECRET_KEY'] = config["APP_SECRET_KEY"]
Bootstrap5(app)
ckeditor = CKEditor(app)

# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    # TODO: Query the database for all the posts. Convert the data to a python list.
    posts = db.session.execute(db.select(BlogPost)).scalars().all()
    return render_template("index.html", all_posts=posts)

# TODO: Add a route so that you can click on individual posts.
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # TODO: Retrieve a BlogPost from the database based on the post_id
    requested_post = db.get_or_404(BlogPost, post_id)
    return render_template("post.html", post=requested_post)


# TODO: add_new_post() to create a new blog post

@app.route("/new-post", methods=["POST", "GET"])
def new_post():

    form = NewPostForm()
    if request.method == "POST":
        date = datetime.now().strftime("$B %d, %Y")
        # textarea = request.form.get('ckeditor')
        textarea = request.form['textarea']
        title = request.form["title"]
        new_post = BlogPost(
            title=request.form["title"],
            subtitle=request.form["subtitle"],
            img_url=request.form["img_url"],
            author=request.form["author"],
            body=request.form["textarea"],
            date=date
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template('make-post.html', form=form, edit=False)

# TODO: edit_post() to change an existing blog post

@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):

    post = db.session.get(BlogPost, post_id)
    form = NewPostForm(
            title=post.title,
            subtitle = post.subtitle,
            textarea = post.body,
            img_url = post.img_url,
            author= post.author
        )
    
    if request.method == "POST":
        post.title=request.form["title"]
        post.subtitle=request.form["subtitle"]
        post.img_url=request.form["img_url"]
        post.author=request.form["author"]
        post.body=request.form["textarea"]

        db.session.commit()

        return redirect(url_for('get_all_posts'))
    return render_template('make-post.html', form=form, edit=True)

# TODO: delete_post() to remove a blog post from the database

@app.route("/delete-post/<int:post_id>")
def delete_post(post_id):
    post = db.session.get(BlogPost, post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('get_all_posts'))

@app.route("/about")
def about():
    return render_template("about.html", ckeditor=ckeditor)


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)

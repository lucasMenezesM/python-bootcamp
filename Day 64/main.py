from flask import Flask, render_template, redirect, url_for, request, jsonify
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from data_base_manager import DataBaseManager
from my_form import MyForm, UpdateForm, AddMovieForm
from dotenv import dotenv_values

config = dotenv_values("Day 64/.env")

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

database = DataBaseManager(app=app)
db = database.db

database.create_movies_table(app=app)
Movie = database.Movie

# ROUTES

@app.route("/")
def home():
    def myFunc(e):
        return e.rating
    movies = database.get_all_movies()
    movies.sort(key=myFunc)

    for index, movie in enumerate(movies):
        movie.raking = len(movies) - index
    db.session.commit()

    return render_template("index.html", movies=movies)


@app.route("/add-page", methods=["GET", "POST"])
def add_movie_page():
    form = AddMovieForm()
    if form.validate_on_submit():
        title = form.title.data
        print(title)
        # database.add_new_movie(title=title)
        return redirect(url_for('movie_options', title=title))
    return render_template("add.html", form=form)


@app.route("/movie-options/<title>")
def movie_options(title):
    movies = database.search_movies(title=title)
    return render_template("select.html", movies=movies)


@app.route("/add-movie/<id>")
def add_new_movie(id):
    movie = database.find_movie_by_id(id=id)
    new_movie = Movie(
        id=movie["id"],
        title = movie["original_title"],
        year = movie["release_date"].split("-")[0],
        description = movie["overview"],
        img_url = "https://image.tmdb.org/t/p/w500"+movie["poster_path"],
        rating = 0,
        review = "...",
        ranking = 0
    )
    database.add_new_movie(movie=new_movie, app=app)
    return redirect(url_for('edit', id=movie["id"]))
    

@app.route("/edit/<int:id>", methods= ["GET", "POST"])
def edit(id):
    form = UpdateForm()
    if form.validate_on_submit():
        movie = database.get_movie(id=id)
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect('/')

    return render_template('edit.html', form=form)

@app.route("/test")
def test():
    pass


@app.route("/delete/<int:id>")
def delete(id):
    database.delete_movie(id=id)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

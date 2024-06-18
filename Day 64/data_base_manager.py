from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
import requests
from dotenv import dotenv_values

config = dotenv_values("Day 64/.env")

class DataBaseManager:
    def __init__(self, app) -> None:
        class Base(DeclarativeBase):
            pass

        self.db = SQLAlchemy(model_class=Base)

        # create the app
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies-collection2.db"
        self.db.init_app(app)

        class Movie(self.db.Model):
            id: Mapped[int] = mapped_column(primary_key=True)
            title: Mapped[str] = mapped_column(unique=True, nullable=False)
            year: Mapped[int] = mapped_column(Integer, nullable=False)
            description: Mapped[str] = mapped_column(String(300), nullable=False)
            rating: Mapped[float] = mapped_column(Float, nullable=False)
            ranking: Mapped[int] = mapped_column(Integer, nullable=False)
            review: Mapped[str] = mapped_column(String(300), nullable=False)
            img_url: Mapped[str] = mapped_column(String, nullable=False)

        self.Movie = Movie
        with app.app_context():
            self.db.create_all()


    def create_movies_table(self, app):
        pass


    def search_movies(self, title) ->list[dict]:
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {config['API_READ_ACCESS_TOKEN']}"
        }
        response = requests.get(
            url=f"https://api.themoviedb.org/3/search/movie?query={title}",
            headers=headers
        )
        data = response.json()["results"]

        return data
    

    def find_movie_by_id(self, id):
        url = "https://api.themoviedb.org/3/movie/"+id
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {config['API_READ_ACCESS_TOKEN']}"
        }
        response = requests.get(
            url=url,
            headers=headers
        )
        movie = response.json()
        return movie


    def add_new_movie(self, movie, app):

        with app.app_context():
            self.db.session.add(movie)
            self.db.session.commit()


    def get_all_movies(self) ->list:
        movies = self.db.session.execute(self.db.select(self.Movie).order_by(self.Movie.title)).scalars().all()
        return movies
    

    def get_movie(self, id):
        movie = self.db.get_or_404(self.Movie, id)
        return movie
    

    def update_movie(self, form, id):
        movie = self.db.get_or_404(self.Movie, id)
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        self.db.session.commit()


    def delete_movie(self, id):
        movie = self.get_movie(id=id)
        self.db.session.delete(movie)
        self.db.session.commit()
        



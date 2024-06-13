from flask import Flask, render_template, request, redirect, url_for
# from book import Book
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

# db = sqlite3.connect("Day 63/books-collection.db")
# cursor = db.cursor()
# # cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# cursor.execute("INSERT INTO books VALUES(523, 'Haddxcxcasdy Potter', 'J. dzzxsdK. Rowliaddsdddasdng', '9.1')")
# db.commit()

app = Flask(__name__)

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)


# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"
# initialize the app with the extension
db.init_app(app)

class Book(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

with app.app_context():
    db.create_all()

# FUNCTIONS

def get_books():
    books = db.session.execute(db.select(Book).order_by(Book.title)).scalars().all()
    return books

def delete_book(id):
    pass

all_books = []

@app.route('/')
def home():
    books = get_books()
    return render_template("index.html", books=books)


@app.route("/add", methods = ["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = Book(title=request.form["title"], author=request.form["author"], rating=float(request.form["rating"]))
        db.session.add(new_book)
        db.session.commit()
        books = get_books()
        print(books[0])

        return redirect(url_for('home'))

    return render_template("add.html")


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_book(id):

    book = db.get_or_404(Book, id)
    print(f"Book found {book.title}")

    if request.method == "POST":
        print("PUT METHOD")
        book.rating = float(request.form["rating"])
        db.session.commit()
        return redirect(url_for('home'))
        
    return render_template('edit.html', book=book)


@app.route("/delete/<int:id>")
def delete_book(id):
    book = db.get_or_404(Book, id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)












'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''
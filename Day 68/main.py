from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
import requests
from dotenv import dotenv_values

config = dotenv_values(".env")

app = Flask(__name__)
app.config['SECRET_KEY'] = config["SECRETE_KEY"]

# CREATE DATABASE

class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return db.session.execute(db.select(User).filter_by(id=user_id)).scalar_one()


# CREATE TABLE IN DB


class User(db.Model, UserMixin):
    def __init__(self) -> None:
        super().__init__()
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html", user=current_user)


@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == "POST":
        password = request.form["password"]
        user_email = request.form["email"]

        user_found = db.session.execute(db.select(User).filter_by(email=user_email)).scalar_one()

        if not user_found:
            hashed_password = generate_password_hash(password=password, salt_length=10)
            print(f"password hashed: {hashed_password}")
            new_user = User(
                name=request.form["name"],
                email=request.form["email"],
                password=hashed_password
            )

            db.session.add(new_user)
            db.session.commit()

            login_user(user_found)
            return render_template('secrets.html', user=new_user)
        else:
            flash("User already registered")
            print("User already registered")

    return render_template("register.html", user=current_user)


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user_password = request.form["password"]
        user_email = request.form["email"]

        user_found = db.session.execute(db.select(User).filter_by(email=user_email)).scalar_one()

        if user_found:
            if check_password_hash(password=user_password, pwhash=user_found.password):
                login_user(user_found)

                print("authorized")
                return render_template('secrets.html', user=current_user)
            else:
                flash("The email or password might be incorrect. Try again")
                print("Not authorized")
                
    return render_template("login.html", user=current_user)


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", user=current_user)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory('static', path="files/cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)

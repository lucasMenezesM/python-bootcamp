from flask import Flask
import random
import database

app = Flask(__name__)

random_number = random.randint(0, 9)


@app.route("/")
def home():
    return "<h1>Guess a number!</h1>"\
            f'{database.home_gif}'


@app.route("/<int:number>")
def guessed_number(number):
    if number > random_number:
        return "<h1>Too high, try again!</h1>"\
                f'{database.too_high}'
    elif number < random_number:
        return "<h1>Too low, try again!</h1>"\
                f'{database.too_low}'
    else:
        return f"<h1>You got it!</h1>"\
                f"{database.happy_gif}"

if __name__ == "__main__":
    app.run(debug=True)
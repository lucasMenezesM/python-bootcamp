from flask import Flask, render_template, redirect, request, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from my_form import MyForm


'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


app = Flask(__name__)
app.secret_key = "some secret string"

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    form = MyForm()
    if form.validate_on_submit():
        print(form.email.data)
        print(form.password.data)
        print(jsonify(request.form))

        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return render_template('success.html')
        else:
            return render_template('denied.html')
    
    # if request.method == "GET":
        
        # if form.validate_on_submit():
        #     return redirect('/success')
        
    return render_template('/login.html', form=form)
        # return render_template("login.html", form=MyForm)
    # else:
    #     print(request.form["email"])
    #     return jsonify(request.form)


if __name__ == '__main__':
    app.run(debug=True)

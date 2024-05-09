from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.users import User

@app.route('/')
def main():
    all_users=User.get_all()
    return render_template('read.html', users=all_users)


@app.route('/users')
def index():
    return render_template("create.html")



@app.route('/create_user', methods = ['POST'])
def create():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    User.create_user(data)
    return redirect('/')




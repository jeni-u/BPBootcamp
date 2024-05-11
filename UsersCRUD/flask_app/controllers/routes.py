from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.user import User

@app.route('/')
def main():
    users = User.getAllUsers()
    return render_template("read.html",users=users)
    

@app.route("/create")
def index():
    return render_template("create.html")

@app.route("/create_user" ,methods = ['POST'])
def create_user():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    User.createUser(data)
    return redirect("/")


@app.route('/show/<int:id>')
def show(id):
    data ={
        'id': id,
    }
    user = User.get_user_by_id(data)
    return render_template("show.html",user=user)


@app.route("/update/<int:id>" ,methods = ['POST'])
def user_update(id):
    data = {
        'id':id,
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    User.update_user(data)
    return redirect("/")

@app.route("/edit/<int:id>")
def edit_user(id):
    data = {
        'id':id
    }
    user=User.get_user_by_id(data)
    return render_template("edit.html",user=user)

@app.route('/delete/<int:id>')
def delete(id):
    data = {
        'id':id
    }
    User.delete_user(data)
    return redirect('/')
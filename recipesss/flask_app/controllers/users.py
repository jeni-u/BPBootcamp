from flask_app import app
from flask import render_template,redirect,request,session
from flask_app.models.user import User
from flask_app.models.recipe import Recipe

from flask import flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def main():

    return render_template("login.html")
    

@app.route("/register")
def index():
    return render_template("register.html")

@app.route('/register_user', methods= ['POST'])
def register():
    if not User.validate_user(request.form):
        return redirect('/register')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    register_user = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password": pw_hash
    }
    user_id = User.createUser(register_user)
    session['user_id'] = user_id
    return redirect('/dashboard')


@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')
    
@app.route('/login_user', methods= ['POST'])
def login_user():
    if not User.validate_login(request.form):
        flash('This user doesnt exists! Check your email', 'emailLogin')
        return redirect(request.referrer)
    user = User.get_email(request.form)
    if user:
        if not bcrypt.check_password_hash(user['password'], request.form['password']):
            flash("Invalid password!", 'passwordLogin')
            return redirect(request.referrer)
        session['user_id']= user['id']
        return redirect ('/dashboard')
    return redirect('/dashboard')


@app.route('/dashboard')
def results():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {"id": session['user_id']}
    user = User.get_user_by_id(data)
    if not user:
        return redirect('/logout')
    recipes = Recipe.getAllRecipes()
    return render_template('dashboard.html', user=user,recipes=recipes)




"""@app.route("/update/<int:id>" ,methods = ['POST'])
def user_update(id):
    data = {
        'id':id,
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    User.update_user(data)
    return redirect("/")"""

"""@app.route("/edit/<int:id>")
def edit_user(id):
    data = {
        'id':id
    }
    user=User.get_user_by_id(data)
    return render_template("edit.html",user=user)"""

"""@app.route('/delete/<int:id>')
def delete(id):
    data = {
        'id':id
    }
    User.delete_user(data)
    return redirect('/')"""
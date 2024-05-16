
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return redirect('/register')

@app.route('/register')
def reg():
    return render_template("index.html")

@app.route('/register_user', methods= ['POST'])
def register():
    if not User.validate_register(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    register_user = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password": pw_hash
    }
    user_id = User.save_user(register_user)
    session['user_id'] = user_id
    flash("You have been registerd!")
    return redirect('/dashboard')

@app.route('/login')
def login():
    return render_template("login.html")
    
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
    data = {
        "id": session['user_id']
    }
    user = User.get_id(data)
    return render_template('dashboard.html', user=user)


@app.route('/logout')
def logout():
    session.clear()
    return redirect ('/')
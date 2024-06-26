
from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo


@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dashboard():
    dojos = Dojo.get_all()
    return render_template('dojo.html', dojos=dojos)

@app.route('/create/dojo', methods = ['POST'])
def create_dojo():
    Dojo.save(request.form)
    return redirect('/dojos')

@app.route('/dojos/<int:id>')
def dojo_dashboard(id):
    data = {
        "id": id
    }
    dojo = Dojo.get_one(data)
    return render_template('ninja_show.html', dojo=dojo)

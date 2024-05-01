from flask_app import app
from flask import render_template

@app.route('/')
def check1():
    return render_template('checker.html')

@app.route('/<int:num>')
def check2(num):
    return render_template('checker2.html',num=num)

@app.route('/<int:num1>/<int:num2>/<color1>/<color2>')
def check3(num1,num2,color1,color2):
    return render_template("checker3.html",num1=num1,num2=num2,color1=color1,color2=color2)
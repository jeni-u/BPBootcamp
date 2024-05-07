from flask_app import app
from flask import render_template,session,redirect,request
import random

@app.route('/')
def random_num():
    session['attempts'] = 0
    random_number = random.randint(1,100)
    session['random_number'] = random_number
    
    return render_template("index.html",random_number=random_number)


    
@app.route('/guess_number', methods=['POST'])
def guess_number():
    session['attempts'] =session['attempts'] + 1

    the_number = int(request.form['number'])
    random_number = session['random_number']
    if session['attempts'] == 5:
        return render_template('lose.html')
    if random_number == the_number:
        return render_template("correct.html",the_number=the_number)
    if random_number > the_number:
        return render_template("low.html")
    if random_number < the_number:
        return render_template("high.html")
    
@app.route("/clear")
def clear():
    session.clear()
    return redirect('/')

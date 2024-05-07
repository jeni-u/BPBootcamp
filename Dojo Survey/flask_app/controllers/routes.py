from flask_app import app
from flask import render_template,session,redirect,request,url_for


@app.route('/')
def form():
    return render_template("form.html")

@app.route('/result', methods=['POST'])
def process():
    name = (request.form.get('name'))
    language = (request.form.get('language'))
    location = request.form.get('location')
    comment = request.form.get('comment')
    return render_template("form_process.html",name=name,language=language,location=location,comment=comment)


@app.route('/back')
def back():
    session.clear()
    return redirect('/')



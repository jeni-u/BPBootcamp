from flask_app import app
from flask import render_template,session,redirect,request

@app.route('/')
def main():
    return render_template('count.html')

@app.route('/counter', methods=['POST'])
def counter():
    session['count'] = session.get('count',0) + 1
    return render_template('count.html', count=session['count'])

@app.route('/thecounter', methods=['POST'])
def thecounter():
    the_counter = int(request.form['thecounter'])
    session['count'] = session.get('count',0) + the_counter
    return render_template('count.html',count=session['count'])


@app.route('/counter2', methods=['POST'])
def countertwo():
    session['count'] = session.get('count',0) + 2
    return render_template('count.html', count=session['count'])

@app.route('/destroy', methods=['POST'])
def destroy():
    session.clear()
    return redirect('/')
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/play")
def first():
    return render_template("boxes.html", num=3, color = 'blue')

@app.route('/play/<int:num>')
def play(num):
    return render_template("boxes.html",num=num, color='blue')


@app.route('/play/<int:num>/<color>')
def third(num,color):
    return render_template("boxes.html",num=num,color=color)

if __name__=="__main__":
    app.run(debug=True)


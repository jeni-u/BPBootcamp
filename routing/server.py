from flask import Flask  
app = Flask(__name__)   
@app.route('/')          
def hello_world():
    return 'Hello World!'  



@app.route('/dojo')
def dojo():
    return 'Dojo'

@app.route('/say/<name>')
def name (name):
    return "Hi " + (str(name)) +"!"

@app.route('/repeat/<int:num>/<emri>')
def repeat(emri,num):
    return emri * num

@app.errorhandler(404)
def page_not_found(e):
    return "Sorry! No response. Try again."



if __name__=="__main__":   
    app.run(debug=True) 
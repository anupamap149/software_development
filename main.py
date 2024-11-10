from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    
   
    return "welcome home"

@app.route('/about')
def about():
        
    return "Welcome to about us page!"

@app.route('/help')
def help():

    return "This is a page for prviding Help "

@app.route("/maths")
def maths():
    a = 5
    b = 10
    c = a+b
    return render_template("maths.html", maths_result=c)

@app.route("/multiply")
def multiply():
    a = 14
    b = 15
    c = 20
    d= a*b*c
    return "This is the result "+ str(d)
    #return render_template("multiply.html", multiply_result=d)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)

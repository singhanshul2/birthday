from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello", methods = ["POST"])
def hello():
    name = request.form.get("name")
    Birth = name=="yes"
    #Birthday = False
    if Birth:
       return render_template("hello.html")
    #else:
     # return ("Wait for your birthday") 

@app.route("/birthday", methods = ["POST"])
def birthday(): 
    name = request.form.get("name")
    return render_template("birthday.html", name=name)    

@app.route("/test", methods = ["POST"])
def test():
   name1 = request.form.get("name")
   return (f"{name1}")



if __name__ = "__main__":
    app.run(debug=False, host='0.0.0.0')
#!/usr/bin/env python
# -*-coding:utf-8-*-

from flask import Flask , url_for , request
from flask import render_template

app = Flask(__name__)

@app.route("/" , methods=['GET','POST']) #Decoradores
def index():
    if request.method == 'POST':
        return "Esto es un POST!"
    else:
        return "Hello World!"
    
@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name=None):
    return render_template("hello.html" , name = name)
    #return "Hola %s" % name

@app.route("/post/<int:post_id>")
def mostrar_post(post_id):
    return "Post %d" % post_id    
    
if __name__ == "__main__":
    #url_for('static' , filename='style.css' )
    app.debug = True
    app.run()
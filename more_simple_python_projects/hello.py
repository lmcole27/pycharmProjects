from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_em(function):
    def wrapper():
        return f"<em><u>{function()}</u></em>"
    return wrapper

def make_blue(function):
    def wrapper():
        return f"<h1>{function()}</h1>"
    return wrapper
        

@app.route("/")
def hello_world():
    return '<h1 style="color:white; background-color:tomato">Hello, World!</h1>'

@app.route("/bye")
# @make_bold
@make_em
@make_blue
def say_bye():
    return "<p>Bye</p>"

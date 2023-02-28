from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # build a graphical representation of a hockey rink
    # and return it to the user



    return render_template('index2.html')
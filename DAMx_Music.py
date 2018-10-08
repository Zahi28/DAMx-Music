from flask import Flask, url_for, redirect
from flask import render_template
app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('home'))


@app.route('/home')
def home():
    return render_template("DAMx_Music.html")


@app.route('/chinese')
def chinese():
    return render_template("DAMx_Music_cn.html")


@app.route('/foreign')
def foreign():
    return render_template("DAMx_Music_ab.html")


if __name__ == '__main__':
    app.run()

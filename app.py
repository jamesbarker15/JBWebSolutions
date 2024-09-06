import flask
from flask import render_template

app = flask.Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/services')
def services():
    return render_template('services.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
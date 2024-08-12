from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "I am flask application serving on port 5000"


@app.route('/about')
def about():
    return "I am about"


@app.route('/home')
def home():
    return "I am home2"

@app.route('/contact')
def contact():
    return "I am contact"


if __name__ == '__main__':
    app.run(debug=True)
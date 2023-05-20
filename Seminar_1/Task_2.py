from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, world!'


@app.route('/about/')
def about():
    return 'О нас'


@app.route('/contacts/')
def contacts():
    return 'Контакты'


if __name__ == '__main__':
    app.run()


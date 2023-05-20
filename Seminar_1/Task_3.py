from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, world!'


@app.route('/about')
def about():
    return 'О нас'


@app.route('/contacts/')
def contacts():
    return 'Контакты'


@app.route('/summ/<int:num1>/<int:num2>/')
def summ(num1, num2):
    return f'Сумма равна {num1} + {num2}'


@app.route('/text/<line>')
def text(line):
    return f'Длина строки равна {len(line)}'


html_templ = """
<h2>Моя первая HTML страница</h2>
<p>Привет, мир!</p>
"""


@app.route('/html/')
def return_html():
    return html_templ


if __name__ == '__main__':
    app.run()
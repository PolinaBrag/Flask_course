from flask import Flask, render_template
from jinja2 import Environment, DictLoader, Template

_news = [
    {'title': 'Новость1', 'description': 'Описание1', 'date': '20.05.2023'},
    {'title': 'Новость2', 'description': 'Описание2', 'date': '21.05.2023'},
    {'title': 'Новость3', 'description': 'Описание3', 'date': '22.05.2023'}
]


app = Flask(__name__)


@app.route('/news/')
def show_news():
    return render_template('news_box.html', news=_news)


if __name__ == '__main__':
    app.run()


from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main_page():
    context = {'title': 'Главная страница'}
    return render_template('shop_main.html', **context)


@app.route('/clothes/')
def clothes():
    context = {'title': 'Одежда'}
    return render_template('shop_clothes.html', **context)


@app.route('/jacket/')
def jacket():
    context = {'title': 'Куртка'}
    return render_template('shop_jacket.html', **context)


@app.route('/shoes/')
def shoes():
    context = {'title': 'Обуыь'}
    return render_template('shop_shoes.html', **context)


if __name__ == '__main__':
    app.run()

from flask import Flask, render_template

app = Flask(__name__)


_students = [
    {'name': 'Иван', 'surname': 'Иванов', 'age': 20, 'avg_score': 35},
    {'name': 'Петр', 'surname': 'Петров', 'age': 21, 'avg_score': 55},
    {'name': 'Олег', 'surname': 'Олегов', 'age': 22, 'avg_score': 38}
]

@app.route('/')
def students():
    return render_template('students.html', students=_students)


if __name__ == '__main__':
    app.run()
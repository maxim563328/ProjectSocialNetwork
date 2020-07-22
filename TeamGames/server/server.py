import sqlite3
import os
from flask import Flask, render_template, url_for, request, g

# Логин администратора - admin
# Ключ администратора - ktF~QEPX49e0Vvg7


# КОНФИГ
DATABASE = 'tmp/teamgames.db'
DEBUG = True
SECRET_KEY = 'Xzr9M1hoKLjgaRHk'

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(DATABASE=os.path.join(app.root_path, 'teamgames.db')))


def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn


# Создание базы данных
def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


def get_db():
    # Соединение с БД
    if not hasattr(g, 'link.db'):
        g.link_db = connect_db()
    return g.link_db


@app.route("/")
def index():
    return render_template('index.html', title="TeamGames")


@app.route("/login", methods=(["POST", "GET"]))
def login():
    # if request.method == 'POST':
    #   user_pass = request.form.
    return render_template('login.html')


if __name__ == "__main__":
    app.run(debug=True)

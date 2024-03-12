from flask import Flask, render_template
from data import db_session
from data.users import User
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
@app.route('/index')
def index():
    param = {}
    param['username'] = "Radmir developer"
    param['title'] = 'Work'
    return render_template('index.html', **param)


def main():
    db_session.global_init("db/mars.db")
    app.run(port=8080, host='127.0.0.1')


if __name__ == '__main__':
    main()

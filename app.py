from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .info import username, password
from users.routes import users


app = Flask(__name__)
app.register_blueprint(users)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{username}:{password}@localhost/db'


@app.route('/')
def start():
    return 'Hello world!'


if __name__ == '__main__':
    app.run()

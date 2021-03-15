from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from info import username, password, host, database
from users.routes import users
from utility import SecretKey

app = Flask(__name__)
app.config['SECRET_KEY'] = SecretKey
app.register_blueprint(users)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{username}:{password}@{host}/{database}'
db = SQLAlchemy(app)


if __name__ == '__main__':
    app.run()

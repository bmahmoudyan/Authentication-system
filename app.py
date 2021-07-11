from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from info import username, password, host, database
from utility import SecretKey
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = SecretKey
# app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{username}:{password}@{host}/{database}'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///authenticator.db"
db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.init_app(app)

from users.routes import users
app.register_blueprint(users)

from main.routes import main
app.register_blueprint(main)

from admin.routes import admin
app.register_blueprint(admin)

if __name__ == '__main__':
    app.run()

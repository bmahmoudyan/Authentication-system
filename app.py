from flask import Flask
from users.routes import users


app = Flask(__name__)
app.register_blueprint(users)


@app.route('/')
def start():
    return 'Hello world!'


if __name__ == '__main__':
    app.run()

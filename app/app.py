from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost:3306/app"
# db = SQLAlchemy(app)


@app.route('/')
def hello_world():
    return '<h1>Hello!!</h1>'


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)

from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["DEBUG"] = True
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="",
    password="",
    hostname="",
    databasename="",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Noted(db.Model):
    __tablename__ = "todo"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(4096))


todo = []


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("homepage.html", todo=Noted.query.all())

    todo = Noted(content=request.form["contents"])
    db.session.add(todo)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/count', methods=["GET", "POST"])
def count():
    return render_template("count.html", total=Noted.query.count())

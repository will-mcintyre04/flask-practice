from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["DEBUG"] = True

from local_settings import SQLALCHEMY_DATABASE_URI

app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI #stashes database in config settings
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299 #Throw away connections that havent been used for 299 seconds
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Comment(db.Model): ##Subclass from db.Model
    __tablename__ = "comments"
     #Equivalent to sqlalchemy.Column. Luckily extension object db provides access to names in sqlalchemy module.
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(4096))
comments = []

@app.route('/', methods=["GET", "POST"])
def index():
    ## HTTP method 'GET' indicates request generally, if used to send: data sent directly in URL. For viewing
    if request.method =="GET":
        return render_template("main_page.html", comments=Comment.query.all())
    ## Otheriwse, POST: used to submit data: data included in request body. When someone clicks button to submit.
    comments.append(request.form["contents"]) #extracts typed text in textarea from browser’s request with name="contents"
    return redirect(url_for("index"))

@app.route('/showdata', methods = ["GET", "POST"])
def showdata():
    return comments

if __name__ == "__main__":
    app.run()
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.config["DEBUG"] = True

comments = []

@app.route('/', methods=["GET", "POST"])
def index():
    ## HTTP method 'GET' indicates request generally, if used to send: data sent directly in URL. For viewing
    if request.method =="GET":
        return render_template("main_page.html", comments=comments)
    ## Otheriwse, POST: used to submit data: data included in request body. When someone clicks button to submit.
    comments.append(request.form["contents"]) #extracts typed text in textarea from browser’s request with name="contents"
    return redirect(url_for("index"))

@app.route('/showdata', methods = ["GET", "POST"])
def showdata():
    return comments

if __name__ == "__main__":
    app.run()
from flask import Flask, render_template

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def hello_world():
    return render_template("main_page.html")

if __name__ == "__main__":
    app.run()
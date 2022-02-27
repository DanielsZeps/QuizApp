from flask import *

app = Flask(__name__)

@app.route("/")
def root():
    return render_template("index.html")

@app.route("/style")
def style():
    return render_template("style.css")

@app.route("/script")
def script():
    return render_template("script.js")

@app.route("/textResponse")
def textResponse():
    return render_template("text.txt")

@app.route("/health")
def health():
    return "OK"

if __name__ == "__main__":
    app.run(debug="true")

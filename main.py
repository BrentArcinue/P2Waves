from flask import Flask, render_template

app = Flask(__name__)


# home screen
@app.route("/home")
@app.route("/")
def home():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True, host = '127.0.0.1',port='3001')
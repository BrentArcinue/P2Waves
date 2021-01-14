from flask import Flask, render_template

app = Flask(__name__)

# home screen

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/")
def login():
    return render_template("login.html")
if __name__ == "__main__":
    app.run(debug=True, host = '127.0.0.1',port='3001')

@app.route('/project/game1')
def game1_route():
    return render_template("game1.html")

@app.route('/project/game2')
def game2_route():
    return render_template("game2.html")

@app.route('/maintemplate')
def maintemplate():
    return render_template("maintemplate.html")
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/no")
def no_page():
    return render_template("no.html")

@app.route("/yes")
def yes_page():
    return render_template("yes.html")

@app.route("/cake")
def cake_page():
    return render_template("cake.html")

@app.route("/letter")
def letter_page():
    return render_template("letter.html")

@app.route("/final")
def final_page():
    return render_template("final.html")

@app.route("/no-ending")
def no_ending_page():
    return render_template("no_final.html")

if __name__ == "__main__":
    app.run(debug=True)

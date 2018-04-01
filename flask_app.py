from flask import Flask, render_template


from datetime import date
today = date.today()

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
def main():
    return render_template("main.html")


@app.route("/humangates")
def humangates():
    return render_template("humangates.html")



@app.route("/cargates")
def cargates():
    return render_template("cargates.html")


@app.route("/staircases")
def staircases():
    return render_template("staircases.html")






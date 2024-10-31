from flask import Flask, render_template, redirect, session, request
import captain

app = Flask(__name__)
app.secret_key = "dortmunderkronenpils" #guter key oder?

@app.route("/")
def start():
    beers = session.get("beers", None)
    return render_template("index.html", dishes=captain.get_food(), beers=beers)
@app.route("/get-beer", methods=["POST"])
def gb():
    dish = request.form["dish"]
    session["beers"] = captain.find_beer(dish)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True, port=5200)
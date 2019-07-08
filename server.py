from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "not very a secret"

@app.route("/")
def index():
    if "your_gold" not in session:
        session["your_gold"] = 0
    return render_template("index.html")

@app.route("/process_money", methods = ["POST"])
def process():
    if request.form["location"] == "farm":
        session["gold"]=random.randint(10,20)
        session["your_gold"] += session["gold"]
    elif request.form["location"] == "cave":
        session["gold"] = random.randint(5,10)
        session["your_gold"] += session["gold"]
    elif request.form["location"] == "house":
        session["gold"]=random.randint(2,5)
        session["your_gold"] += session["gold"]
    else:
        session["gold"]=random.randint(-50,50)
        session["your_gold"] += session["gold"]
    session["location"] = request.form["location"]
    return redirect("/")

@app.route("/reset", methods=["Post"])
def reset():
    session.pop("gold")
    session.pop("location")
    session.pop("your_gold")
    return redirect("/")



#------------------------
if __name__ == "__main__":
    app.run(debug=True)
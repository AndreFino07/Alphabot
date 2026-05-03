from flask import Flask, render_template, request
from AlphaBot import AlphaBot

app = Flask(__name__)
a = AlphaBot()

@app.route("/", methods =["GET"])
def index():
    return render_template ("index.html")

@app.route("/movimento", methods =["POST", "GET"])
def result():
    movimento = request.form.get("mov")
    if movimento == "avanti":
        a.forward()
        print("avanti")
    elif movimento == "indietro":
        a.backward()
        print("indietro")
    elif movimento == "sinistra":
        a.left()
        print("sinistra")
    elif movimento == "destra":
        a.right()
        print("destra")
    elif movimento == "stop":
        a.stop()
        print("stop")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
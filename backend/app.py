from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def home():
    return "SafarShield backend is running!"


@app.route("/register", methods=["POST"])
def register_tourist():
    name = request.form["name"]
    travel_type = request.form["travel_type"]

    return f"Tourist {name} registered as a {travel_type} traveler."


if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request
import random

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/rockpaperscissors", methods=["GET", "POST"])
def rockpaperscissors():
    input = request.form.get("input")
    bot_input = random.choice(["rock", "paper", "scissors"])

    if (
        (input == "rock" and bot_input == "scissors")
        or (input == "paper" and bot_input == "rock")
        or (input == "scissors" and bot_input == "paper")
    ):
        output = "You Win!"
    elif (
        (input == "rock" and bot_input == "rock")
        or (input == "paper" and bot_input == "paper")
        or (input == "scissors" and bot_input == "scissors")
    ):
        output = "It's a draw!"
    elif input is None:
        output = input = bot_input = ""
    else:
        output = "You Lose!"

    return render_template(
        "rockpaperscissors.html",
        input=input,
        bot_input=bot_input,
        result=output
    )


def process_query(q):
    if "dinosaurs" in q:
        return "Dinosaurs ruled the Earth 200 million years ago"
    elif "name" in q:
        return "Team_team"
    return "Unknown"


@app.route("/query", methods=["GET"])
def query():
    q = request.args.get('q')
    return process_query(q)

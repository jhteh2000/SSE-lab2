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
    elif "plus" in q:
        number = []
        q = q.strip("?")
        for word in q.split():
            if word.isdigit():
                number.append(word)
        return (str(int(number[0]) + int(number[1])))
    elif "minus" in q:
        number = []
        q = q.strip("?")
        for word in q.split():
            if word.isdigit():
                number.append(word)
        return (str(int(number[0]) - int(number[1])))
    elif "multiplied" in q:
        number = []
        q = q.strip("?")
        for word in q.split():
            if word.isdigit():
                number.append(word)
        return (str(int(number[0]) * int(number[1])))
    elif "largest" in q:
        number = []
        q = q.strip("?")
        for word in q.split(", "):
            if word.isdigit():
                number.append(word)
        return (max(number))
    elif "cube" in q:
        number = []
        num_cube_sqr = []
        q = q.strip("?")
        for word in q.split(", "):
            if word.isdigit():
                number.append(word)
        for i in range(len(number)):
            if (round(int(number[i]) ** (1/6)) ** 6 == int(number[i])):
                num_cube_sqr.append(number[i])
        result = ", ".join(num_cube_sqr)
        return result
    elif "primes" in q:
        number = []
        num_prime = []
        q = q.strip("?")
        for word in q.split(", "):
            if word.isdigit():
                number.append(word)

        for i in range(len(number)):
            flags_prime = True
            if int(number[i]) <= 1:
                flags_prime = False
            elif int(number[i]) == 2:
                flags_prime = True
            elif int(number[i]) % 2 == 0:
                flags_prime = False
        
            # Check for divisibility up to the square root of n
            for j in range(3, int(int(number[i])**0.5) + 1, 2):
                if int(number[i]) % j == 0:
                    flags_prime = False
            
            if (flags_prime == True):
                num_prime.append(number[i])

        result = ", ".join(num_prime)
        return result
    return "Unknown"


@app.route("/query", methods=["GET"])
def query():
    q = request.args.get('q')
    return process_query(q)

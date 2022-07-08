#!/usr/bin/env python3
"""Alta 3 Flask Final Project
   Patrick Haggerty"""

from flask import Flask
from flask import request
from flask import redirect
from flask import jsonify
from flask import render_template

app= Flask(__name__)

jedi = [{
        "name": "Obi-Wan Kenobi",
        "age": 57,
        "lightsaber color": "blue",
        "apprentices": ["Anakin Skywalker", "Luke Skywalker"],
        "alias": "Ben Kenobi"
        },
        {
        "name": "Mace Windu",
        "age": 53,
        "lightsaber color": "purple",
        "apprentices": ["Depa Billaba", "Echuu Shen-Jon"],
        "alias": "Master Windu"
        },
        {
        "name": "Yoda",
        "age": 900,
        "lightsaber color": "green",
        "apprentices": ["Dooku", "Mace Windu"],
        "alias": "Master Yoda"
        }]
@app.route("/jedi")
def showjedi():
    # render the template with the value of score for marks
    # marks is a jinja var in the template
    return render_template("jedi.html", jedi = jedi)

@app.route("/")
def index():
    # jsonify returns legal JSON
    return jsonify(jedi)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)


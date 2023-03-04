from flask import render_template
from coachmentor import app, db
from coachmentor import mentors, bookings


@app.route("/")
def home():
    return render_template("base.html")
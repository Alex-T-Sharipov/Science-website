import os
import sqlite3

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

#global variables

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
# if starting from scratch, create an empty db file by using the line below:
# open("birthdays.db", "w").close()
# opens birthdays.db file as database using CS50 library
db = SQL("sqlite:///birthdays.db")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        # TODO: Add the user's entry into the database
        
        name = request.form.get("Name")
        print(name)
        month = request.form.get("Month")
        print(month)
        day = request.form.get("Day")
        print(day)
        
        if not name:
            return render_template("error.html", message = "Missing name")
        if not month:
            return render_template("error.html", message = "Missing month")
        if not day:
            return render_template("error.html", message = "Missing year")
        if int(month) < 1 or int(month) > 12:
            return render_template("error.html", message = "Month out of range")
        if int(day) < 1 or int(day) > 31:
            return render_template("error.html", message = "Day out of range")
        print("line 43")
        db.execute("INSERT INTO birthdays (name, month, day) VALUES(?, ?, ?)", name, month, day)
        print("line 45")
        return redirect("/")

    else:

        # TODO: Display the entries in the database on index.html
        print("line 51")
        rows = db.execute("SELECT * FROM birthdays")
        print("line 53")
        return render_template("index.html", rows = rows)



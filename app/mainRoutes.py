from app import app
from flask import render_template

@app.route("/")
def mainRoute():
  return render_template("index.html")
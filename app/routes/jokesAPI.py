from app import app
from app.routes import Joking

jokes = Joking

@app.route("/randomJokes")
def randomJokes():
  return {"joke" : jokes.random_joke()}
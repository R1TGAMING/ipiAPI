from app import app

@app.route("/")
def mainRoute():
  return {"message" : "Hello World!"}
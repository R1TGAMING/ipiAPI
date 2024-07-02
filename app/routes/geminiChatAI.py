from app.routes import genai
import os
from dotenv import load_dotenv
from flask import request
from app import app

# Load env variables and configure the key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_KEY"))

# Create the models
model = genai.GenerativeModel('gemini-1.5-flash')

@app.get("/ai/chatai")
async def chatAi() :
  req = request.args.get("prompt")
  response =  model.generate_content(req)

  return {"response" : response.text}
  


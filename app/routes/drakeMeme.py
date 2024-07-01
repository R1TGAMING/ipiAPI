from app import app
from app.routes import requests, base64, io
from flask import send_file, request
from PIL import Image, ImageDraw, ImageFont

@app.get("/drakeMeme")
def image() :
  # Get Text From Query
  text1 = str(request.args.get("text1"))
  text2 = str(request.args.get("text2"))

  # Open The Image And Draw The Text From Query
  Drake = Image.open("app/static/images/drakeMeme.jpeg")
  img = ImageDraw.Draw(Drake)
  font = ImageFont.truetype("app/static/fonts/ObelixProB-cyr.ttf", 20)
  _, _, w, h = img.textbbox((0,0), text1, font=font)
  W, H = Drake.size
  img.text((300, 100), text=text1, fill=(255, 255, 255), font=font, stroke_fill = (0,0,0), stroke_width=2)
  img.text((300,350), text = text2, fill=(255, 255, 255), font=font, stroke_fill = (0,0,0), stroke_width = 2)
  
  # Buffer The Image And Return The Image
  bytes = io.BytesIO()
  saveImage = Drake.save(bytes, format="JPEG")
  bytes.seek(0)
  
  return send_file(bytes, mimetype="image/jpeg")
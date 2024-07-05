from app import app
from PIL import Image, ImageDraw, ImageFont
from app.routes import requests, base64, io
from flask import request, send_file

@app.get("/customMemes")
def customMemes() :
  imageQuery = str(request.args.get("img"))
  #posXQuery = request.args.get("posX")
  #posYQuery = request.args.get("posY")
  #textQuery = request.args.get("text")

  req = requests.get(imageQuery)
  try :
    image = Image.open(io.BytesIO(req.content))
    dst = Image.new("RGB", (image.width, image.height))
    dst.paste(image)
    ImageDraw.Draw(dst)
    bytes = io.BytesIO()
    save = dst.save(bytes, format="JPEG")
    bytes.seek(0)
    
    return send_file(io.BytesIO(bytes.read()), mimetype="image/jpeg")
    
  except Exception as e :
    return {"error" : e}
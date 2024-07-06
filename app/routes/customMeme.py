from app import app
from PIL import Image, ImageDraw, ImageFont
from app.routes import requests, base64, io
from flask import request, send_file

@app.get("/customMeme")
def customMemes() :
  imageQuery = str(request.args.get("img"))
  posXQuery = int(request.args.get("posX")) 
  posYQuery = int(request.args.get("posY")) 
  textQuery = str(request.args.get("text"))

  req = requests.get(imageQuery)
  try :
    image = Image.open(io.BytesIO(req.content))
    dst = Image.new("RGB", (image.width, image.height))
    dst.paste(image)

    
    draw = ImageDraw.Draw(dst)
    font = ImageFont.truetype("app/static/fonts/ObelixProB-cyr.ttf", 80)
    W, H = image.size
    draw.text((W / 2 + posXQuery, H / 2 + posYQuery), text=textQuery, fill=(255, 255, 255), font=font, stroke_fill = (0,0,0), stroke_width=2)
    
    bytes = io.BytesIO()
    save = dst.save(bytes, format="JPEG")
    bytes.seek(0)
    
    return send_file(io.BytesIO(bytes.read()), mimetype="image/jpeg")
    
  except Exception as e :
    return {"error" : e}
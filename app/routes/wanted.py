from app import app
from app.routes import requests, base64, io
from flask import send_file, request
from PIL import Image, ImageDraw, ImageFont


def concat(img1, img2) :
  # Open The Images
  img1 = Image.open(img1)
  img2 = Image.open(io.BytesIO(img2))

  ImageDraw.Draw(img1)
  ImageDraw.Draw(img2)
  # Get The Width And Height Of The Images
  height = 536
  W, H = img1.size
  ratio = W / H

  #Resizing The Image To Center It
  resize = img2.resize((int(ratio * height + 145), height))
  wanted = img1.copy()

  # Paste The Images And Make It To Bytes
  wanted.paste(resize, (100, 330))
  bytes = io.BytesIO()
  wanted.save(bytes, format="JPEG")
  bytes.seek(0)
  return bytes

@app.get("/wanted")
def imagewanted() :
  try : 
  # Get Image URL
   url = str(request.args.get("url"))
   req = requests.get(url)
   wantedImage = "app/static/images/wanted.jpeg"
   res = concat(wantedImage, req.content)
  
   return send_file(io.BytesIO(res.read()), mimetype="image/jpeg")
  except Exception as e :
    return {"error" : e}


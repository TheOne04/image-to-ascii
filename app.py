from flask import Flask, render_template, request
from PIL import Image
from ascii_converter import convert_to_ascii

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("upload.html")

@app.route("/ascii", methods=["POST"])
def ascii():
    file = request.files["infile"]
    image = Image.open(file)

    ascii_text = convert_to_ascii(image)


    return render_template("result.html", art=ascii_text)

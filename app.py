from flask import Flask, render_template, request, redirect
from PIL import Image
from ascii_converter import convert_to_ascii

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("upload.html")

@app.route("/ascii", methods=["GET", "POST"])
def ascii():
    if request.method == 'POST':

        file = request.files["infile"]
        image = Image.open(file)

        ascii_text = convert_to_ascii(image)


        return render_template("result.html", art=ascii_text)
    else:
        return redirect("/")
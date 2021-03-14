from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("index.html")
	
@app.route("/embed")
def embed():
	color = request.args.get('color')
	title = request.args.get('title')
	description = request.args.get('description')
	image = request.args.get('image')
	smallimage = request.args.get('smallimage')
	if smallimage == "enabled":
		return render_template("embed_smallimage.html", description = description, title = title, color = color, image = image)
	else:
		return render_template("embed.html", description = description, title = title, color = color, image = image)

@app.route("/favicon.ico")
def favicon():
	return send_from_directory(app.root_path, "favicon.ico")

app.run("0.0.0.0")
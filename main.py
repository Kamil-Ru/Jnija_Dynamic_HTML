from flask import Flask, render_template
import requests

app = Flask(__name__)

respond = requests.get("https://api.npoint.io/4af156202f984d3464c3")
result = respond.json()


@app.route('/')
def home():
    return render_template("index.html", data=result)


@app.route('/<int:id>')
def posts(id):
    for post in result:
        if post["id"] == id:
            return render_template("post.html", id=id, data=post)


if __name__ == "__main__":
    app.run(debug=True)

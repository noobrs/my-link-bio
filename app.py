from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    links = [
        {"site_name": "OpenAI", "url": "https://openai.com"},
        {"site_name": "Python", "url": "https://www.python.org"},
        {"site_name": "Flask", "url": "https://flask.palletsprojects.com"},
    ]
    return render_template("index.html", links=links)


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)

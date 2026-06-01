from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

links = [
    {"site_name": "OpenAI", "url": "https://openai.com"},
    {"site_name": "Python", "url": "https://www.python.org"},
    {"site_name": "Flask", "url": "https://flask.palletsprojects.com"},
]


@app.route("/")
def index():
    return render_template("index.html", links=links)


@app.route("/add", methods=["POST"])
def add_link():
    site_name = request.form.get("site_name", "").strip()
    url = request.form.get("url", "").strip()

    if site_name and url:
        links.append({"site_name": site_name, "url": url})

    return redirect(url_for("index"))


@app.route("/delete/<int:link_index>", methods=["POST"])
def delete_link(link_index):
    if 0 <= link_index < len(links):
        links.pop(link_index)

    return redirect(url_for("index"))


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)

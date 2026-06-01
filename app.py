from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

NOT_AVAILABLE = "Not Available"
OG_FIELDS = {
    "title": "og:title",
    "description": "og:description",
    "image_url": "og:image",
}


def get_meta_content(soup, property_name):
    meta_tag = soup.find("meta", property=property_name)
    if not meta_tag:
        return NOT_AVAILABLE

    content = meta_tag.get("content", "").strip()
    return content or NOT_AVAILABLE


def fetch_open_graph_metadata(url):
    import requests
    from bs4 import BeautifulSoup

    metadata = {field: NOT_AVAILABLE for field in OG_FIELDS}

    try:
        response = requests.get(
            url,
            headers={"User-Agent": "my-link-bio/1.0"},
            timeout=5,
        )
        response.raise_for_status()
    except requests.RequestException:
        # If the page cannot be fetched, every Open Graph field keeps the fallback value.
        return metadata

    soup = BeautifulSoup(response.text, "html.parser")

    for field, property_name in OG_FIELDS.items():
        metadata[field] = get_meta_content(soup, property_name)

    return metadata


def build_link(site_name, url, metadata=None):
    metadata = metadata or {field: NOT_AVAILABLE for field in OG_FIELDS}
    return {"site_name": site_name, "url": url, **metadata}


links = [
    build_link("OpenAI", "https://openai.com"),
    build_link("Python", "https://www.python.org"),
    build_link("Flask", "https://flask.palletsprojects.com"),
]


@app.route("/")
def index():
    return render_template("index.html", links=links)


@app.route("/add", methods=["POST"])
def add_link():
    site_name = request.form.get("site_name", "").strip()
    url = request.form.get("url", "").strip()

    if site_name and url:
        metadata = fetch_open_graph_metadata(url)
        links.append(build_link(site_name, url, metadata))

    return redirect(url_for("index"))


@app.route("/edit/<int:link_index>", methods=["GET", "POST"])
def edit_link(link_index):
    if not 0 <= link_index < len(links):
        return redirect(url_for("index"))

    link = links[link_index]

    if request.method == "POST":
        site_name = request.form.get("site_name", "").strip()
        url = request.form.get("url", "").strip()

        if site_name and url:
            metadata = fetch_open_graph_metadata(url)
            link.update(build_link(site_name, url, metadata))

        return redirect(url_for("index"))

    return render_template("edit.html", link=link, link_index=link_index)


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

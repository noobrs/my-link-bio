# My Link Bio

## Project Overview

A beginner-friendly Flask link-in-bio app for collecting personal, project, or resource links on one styled page. Users can add, edit, and delete link cards, and the app attempts to fetch Open Graph metadata from each URL to show richer previews when available.

## Features

- Home page that displays a styled list of link cards.
- Add new links with a site name and URL.
- Edit existing links from a pre-filled form.
- Delete links from the link list.
- Fetch Open Graph metadata (`og:title`, `og:description`, and `og:image`) for newly added or edited URLs.
- Show rich preview cards when metadata is available.
- Show a warning and fallback card state when a URL cannot provide preview metadata.
- Static About and Contact pages.
- JSON health check endpoint for uptime monitoring.
- Custom 404 and 500 error pages.

> **Note:** Links are stored in an in-memory Python list. Any links added, edited, or deleted while the app is running will reset when the server restarts.

## Tech Stack

- Python
- Flask
- Jinja templates
- HTML
- CSS
- Requests
- Beautiful Soup
- Gunicorn for production serving
- Render configuration for deployment

## Dependencies

The Python dependencies are listed in `requirements.txt`:

- Flask
- Gunicorn
- Requests
- Beautiful Soup 4

## Folder Structure

```text
my-link-bio/
├── app.py                         # Main Flask application, routes, and in-memory link data
├── requirements.txt               # Python package dependencies
├── render.yaml                    # Render deployment configuration
├── LICENSE                        # Apache 2.0 license text
├── README.md                      # Project documentation
├── course-specific/               # Course support documentation
│   ├── introduction.md
│   └── learning-objectives.md
├── static/
│   └── style.css                  # App styling
└── templates/
    ├── 404.html                   # Custom 404 page
    ├── 500.html                   # Custom 500 page
    ├── about.html                 # About page
    ├── contact.html               # Contact page
    ├── edit.html                  # Edit link form
    └── index.html                 # Home page and add-link form
```

## Setup

### Prerequisites

- Python 3.10 or newer is recommended.
- `pip` for installing Python packages.

### 1. Clone the repository

```bash
git clone <repository-url>
cd my-link-bio
```

### 2. Create and activate a virtual environment

On macOS or Linux:

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Environment Variables

| Variable | Required | Description |
| --- | --- | --- |
| `SECRET_KEY` | No | Flask secret key used for flash messages and session signing. If omitted, the app uses a development fallback value from `app.py`. Set this to a strong, private value in production. |

## Running the Project Locally

Start the Flask development server:

```bash
python app.py
```

Then open the local URL shown in your terminal, usually:

```text
http://127.0.0.1:5000
```

## Usage Examples

### Add a link

1. Open the home page.
2. Enter a site name, such as `OpenAI`.
3. Enter a full URL, such as `https://openai.com`.
4. Select **Add Link**.

The app saves the link in memory and attempts to fetch Open Graph preview data for the card.

### Edit a link

1. Select **Edit** on a link card.
2. Update the site name or URL.
3. Select **Save Changes**.

### Delete a link

1. Select **Delete** on a link card.
2. The app removes the link from the in-memory list and returns to the home page.

### Check app health

Visit `/health` in a browser or run:

```bash
curl http://127.0.0.1:5000/health
```

A healthy app returns JSON with a status of `ok` and the current server time.

## Screenshots

Screenshots can be added here after running the app locally or deploying it.

```markdown
![Home page screenshot](docs/screenshots/home.png)
```

## Endpoint Summary

| Method | Path | Description |
| --- | --- | --- |
| `GET` | `/` | Displays the link-in-bio home page and add-link form. |
| `POST` | `/add` | Adds a new link from submitted form data, fetches metadata, and redirects home. |
| `GET` | `/edit/<link_index>` | Displays a pre-filled edit form for the selected link. |
| `POST` | `/edit/<link_index>` | Updates the selected link and redirects home. |
| `POST` | `/delete/<link_index>` | Deletes the selected link and redirects home. |
| `GET` | `/about` | Displays the About page. |
| `GET` | `/contact` | Displays the Contact page. |
| `GET` | `/health` | Returns JSON health status and server time. |

The app also renders custom pages for 404 and 500 errors.

## Build

There is no separate build step for this Flask application. Install the Python dependencies and run the app directly.

## Tests

This repository does not currently include an automated test suite.

To perform a basic smoke check, run:

```bash
python app.py
```

Confirm that the Flask server starts without errors, then open the local URL in a browser.

## Deployment Notes

This repository includes a `render.yaml` file configured for Render:

- Build command: `pip install -r requirements.txt`
- Start command: `gunicorn app:app`
- Service type: Python web service on Render's free plan

For production deployments, set a strong `SECRET_KEY` environment variable in your hosting provider.

Because link data is stored in memory, production data will not persist across deploys, server restarts, or multiple running instances. Add a database or other persistent storage before using this as a long-term public link manager.

## Contributing

Contributions are welcome. To propose a change:

1. Fork the repository.
2. Create a feature branch.
3. Make a focused change with clear, beginner-friendly code.
4. Run the local smoke check with `python app.py`.
5. Open a pull request with a summary of the change and any testing performed.

Please keep functions small, use clear variable names, and avoid documenting behavior that is not implemented in the code.

## License

This project is licensed under the Apache License 2.0. See [`LICENSE`](LICENSE) for details.

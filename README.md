## OpenAI Codex 101: From Idea to Deployed App

### Project Overview

Throughout this course, you build a personal link-in-bio page using OpenAI Codex. Users add their URLs, and the app automatically pulls Open Graph metadata (titles, descriptions, and preview images) to generate rich link cards. The app is built with Python and Flask, uses BeautifulSoup for metadata scraping, and deploys to Render. The app also includes static About and Contact pages so visitors can learn more and find an email address.

This article contains every prompt used in the course, organized by video. You can copy and paste them directly into the Codex web interface at [chatgpt.com/codex](https://chatgpt.com/codex).

### Tools and Accounts You Need

* **ChatGPT account** on a paid plan (Plus, Pro, Business, Edu, or Enterprise)
* **GitHub account** (free at github.com)
* **Render account** (free tier at render.com)
* **UptimeRobot account** (free at uptimerobot.com)

### Setup

Install dependencies and run the Flask app locally:

```bash
pip install -r requirements.txt
python app.py
```

### Dependencies

The app depends on these Python packages, which are listed in `requirements.txt`:

* Flask
* BeautifulSoup
* Requests
* Gunicorn

### Features

* Home page at `/` for viewing, adding, editing, and deleting link cards.
* Open Graph metadata scraping for richer link previews when users add or edit URLs.
* Warning feedback and distinct card styling when a saved URL does not return preview metadata.
* About page at `/about` with a short profile message.
* Contact page at `/contact` with a short message and the email address `hello@example.com`.

---

## Prompts by Video

### Chapter 1, video 1: Set Up Your Codex Environment

After connecting your GitHub repo, use this prompt to verify Codex can see your project:

* *Tell me about this code base*

### Chapter 1, video 2: Create Your First AGENTS.md File

No Codex prompt for this video. You create the AGENTS.md file manually in your GitHub repository.

### Chapter 1, video 3: Write Your First Task

Your first focused prompt for the link-in-bio app:

* *Create a single route at the root URL that renders a page titled My Links. Display a hardcoded list of three URLs, each showing the site name and linking to the URL. Use basic HTML with no CSS for now.*

### Chapter 2, video 1: Review and Evaluate the Output

Submit this prompt and watch how Codex executes it step by step:

* *Add a second route at /about that displays a heading that says About and a short paragraph that says This is my personal link page. Add a navigation link to the about page at the top of the homepage.*

### Chapter 2, video 2: Deploy Your App to a Live URL

Create the files Render needs to deploy your app. Submit these prompts one at a time:

**Prompt 1: Generate requirements.txt**

* *Generate a requirements txt that includes flask with its current version.*

**Prompt 2: Add production dependencies**

* *Update the requirements.txt file with gunicorn, requests, and beautifulsoup4 with their current versions.*

**Prompt 3: Create Render config**

* *Create a file called render.yaml in the project root that configures a free web service using the build command pip install -r requirements.txt and the start command gunicorn app:app.*

### Chapter 2, video 3: Iterate and Add Features

Submit these prompts one at a time. After each one, push the changes and check your live URL.

**Prompt 1: Add a form and in-memory storage**

* *Add a form to index.html above the links list with two input fields: one for the site name and one for the URL. Add a submit button labeled Add Link. In app.py, create a POST route at slash add that reads the form data and stores it. For now, store links in a Python list in memory. After storing, redirect back to the homepage. Update the homepage route to pass the links list to the template, and update index.html to loop through the list and display each link.*

**Prompt 2: Add styling**

* *Add Tailwind CSS styling to the link-in-bio page. Center the content on the page with a max width of 600 pixels. Style each link as a card with rounded corners, a light border, and padding. Style the form inputs and button to match. Add a simple color scheme. Put the CSS in a static folder in a file called style.css and link it in the templates.*

**Prompt 3: Add delete functionality**

* *Add a Delete button to each link card on the homepage. When clicked, it should remove that link from the in-memory store and redirect back to the homepage. Add the necessary route.*

**Prompt 4: Add edit functionality**

* *Add an Edit button to each link card on the homepage. When clicked, it should open a form pre-filled with the current site name and URL. Submitting the form should update the link in memory and redirect back to the homepage. Add the necessary route and template.*

### Chapter 3, video 1: Add Live Data to Your App

Submit these prompts one at a time to add Open Graph metadata scraping:

**Prompt 1: Add OG metadata scraping**

* *Add columns to each link card on the homepage that represent the title, description, and image URL. Determine this information by using the requests library to fetch the page HTML for the link the user provides when adding a new link and use Beautiful Soup to parse the website at that link. Extract the og:title, og:description, and og:image meta tags. If a tag is missing, store a string that says 'Not Available' in the columns in the link card.*

**Prompt 2: Update template for rich cards**

* *Update index.html to display each link card as a rich card. If an image URL exists, show the image at the top of the card. Display the title in bold below the image. Display the description below the title. Keep the URL as a clickable link at the bottom of the card. If values aren't available, continue to display the link card as before with static text.*

### Chapter 3, video 2: Extend Codex with MCP

First, ask Codex how to set up MCP:

**Prompt 1: Plan the MCP setup**

* */plan How do I give you access to the Context7 MCP server in this environment?*

**Prompt 2: Use MCP with a real task**

* *Configure the Context7 MCP server in this environment. Add Flask error handlers for 404 and 500 errors to app.py. Each handler should render a custom error template. Use context7 MCP server to reference the current Flask documentation for error handling. Make sure to let me know the specific links on Context7 that you referenced to find the Flask error handling standards and procedures. Do not complete the task if you're unable to access Context7. If you encounter errors, let me know the exact details.*

### Chapter 3, video 3: Teach Codex Reusable Skills

Create a skill, then test it with a real task:

**Prompt 1: Create the README skill**

* *Create a new skill called "update-readme" at .codex/skills/ that teaches Codex how to keep the project README current. The SKILL.md should have the name update-readme and a description that says: Use this skill when a new feature, route, or dependency is added to the project. The instructions should tell Codex to update README.md with a description of what changed, how to use the new feature, and any new dependencies that were added. Keep the README organized with sections for Project Overview, Features, Setup, and Dependencies. Follow the existing README format if one exists. Once you create the skill, let me know the exact path where it was created. Make sure you can execute the skill.*

**Prompt 2: Test the skill with a new feature**

* *Add a contact page where users can see an email address and a short message.*

### Chapter 3, Video 4: Package a Codex Plugin

Create a plugin manifest that bundles your skill and MCP config:

**Prompt 1: Create the plugin manifest**

* *Create a Codex plugin in .codex-plugin/ with a plugin.json manifest file. Set the name to flask-project-toolkit, version to 1.0.0, and description to "A plugin that bundles a README documentation skill and Context7 MCP for Flask projects." Set the author to your name. In the skills tag, reference the existing skill at .agents/skills/update-readme/SKILL.md. In the mcpServers section, add a Context7 server entry with the command npx and arguments -y @upstash/context7-mcp. Set the interface display name to Flask Project Toolkit and the short description to Auto-documenting README and live Flask docs in one install. Here is an example of JSON manifest file that you can follow, but only include the fields I've requested: { "name": "Name here", "version": "1.0.0", "description": "Description here", "author": { "name": "Your team", "email": "team@example.com", "url": "[https://example.com](https://example.com)" }, "skills": "./skills/", "mcpServers": "./.mcp.json", "interface": { "displayName": "Display name here", "shortDescription": "Reusable skills and apps", "developerName": "Developer name" } }*

### Chapter 4, video 1: Debug and Fix a Live App

These prompts add logging and improve error handling for broken URLs:

**Prompt 1: Add logging**

* *Add Python logging to app.py. Import the logging module and configure it at the INFO level. In the fetch_open_graph_data function, log a warning when a request fails that includes the URL and the error message. In the add route, log an info message when a new link is successfully added and a warning when metadata could not be retrieved for a URL.*

**Prompt 2: Improve error handling and UX**

* *Update the add route in app.py so that after fetching metadata, if all three metadata fields, title, description, and image URL, come back as Not Available, flash a warning message that says We saved your link but could not retrieve a preview for that URL. Also add a visual indicator to the link card template so cards with missing metadata are styled differently from cards with full previews.*

### Chapter 4, video 2: Set Up Monitoring for Your Live App

Add a health check endpoint to your app:

* *Add a health check route at /health in app.py. The route should return a JSON response with status ok, the current server time, and a 200 status code. If an unhandled exception occurs, return status error and a 500 status code.*

### Chapter 5, video 1: Your Turn: Build, Deploy, and Share

No specific prompts for this video.

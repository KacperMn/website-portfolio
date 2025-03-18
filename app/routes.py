import json
from flask import Blueprint, render_template

main = Blueprint('main', __name__)

# Load project data from JSON file
with open("app/static/projects.json") as f:
    projects = json.load(f)

@main.route("/")
def home():
    return render_template("index.html")

@main.route("/about")
def about():
    return render_template("about.html")

@main.route("/projects")
def projects_page():
    return render_template("projects.html", projects=projects)

@main.route("/contact")
def contact():
    return render_template("contact.html")
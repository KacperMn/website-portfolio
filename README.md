# flask-project
This is a Flask dynamic portfolio website. It serves as a simple display of my projects, skills, and professional experience.

## Project Structure
```
website-portfolio/
├── app.py
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   └── static/
│       ├── css/
│       │   └── styles.css
│       └── js/
│           └── scripts.js
├── requirements.txt
└── README.md
```

### Features
- Modular structure using Flask's `Blueprint`.
- Dynamic HTML templates with Jinja2.
- Reusable base layout (`base.html`) with `{% block %}` for content injection.
- Static files for custom CSS and JavaScript.

### Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd flask-project
   ```
3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

### Running the Application
To run the Flask application:
1. Start the application using Python:
   ```bash
   python app.py
   ```
2. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

### Adding New Pages
1. Create a new HTML file in the `templates/` directory.
2. Extend `base.html` and define the `{% block content %}` for the page.
3. Add a new route in `routes.py` to serve the page.

### Further steps
1. Create 'about.html', 'projects.html', and 'contact.html'.
2. Create a dynamic display of my projects in 'projects.html'.
3. Create a contact form in 'contact.html'.
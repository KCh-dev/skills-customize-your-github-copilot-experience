# 📘 Assignment: Intro to Web Apps with Flask

## 🎯 Objective

Build a simple web application using the Flask framework. Students will create routes, render HTML templates, and handle form input to learn the basics of web development in Python.

## 📝 Tasks

### 🛠️ Set Up Flask and Create Routes

#### Description
Create a Flask application with at least two routes: a home page and an about page.

#### Requirements
Completed program should:

- Create a Flask app instance in `starter-code.py`.
- Define a route for `/` that returns a welcome message or HTML page.
- Define a route for `/about` that returns a short description of the app.
- Use Flask route decorators to map URLs to view functions.

### 🛠️ Render an HTML Template

#### Description
Render a template for the home page using Flask's `render_template` function.

#### Requirements
Completed program should:

- Create a `templates/` folder and add a simple `home.html` file.
- Use `render_template('home.html')` in the home route.
- Include a title and a short introduction message on the page.
- Use template variables to pass a message or heading from Python to HTML.

### 🛠️ Handle Form Input

#### Description
Add a form to the site that lets users submit their name and receive a personalized greeting.

#### Requirements
Completed program should:

- Create a route for `/greet` that accepts `POST` requests.
- Build a form in `home.html` or a new template where users enter their name.
- Read the submitted name from `request.form` and display a greeting.
- Show a response page or the home page with the greeting included.

### 🛠️ Run and Test the App

#### Description
Start the Flask development server and verify the pages work in a browser.

#### Requirements
Completed program should:

- Run the app with `python starter-code.py` or `flask run`.
- Load the home page and the about page in a browser.
- Submit the form and confirm that the greeting appears correctly.
- Optionally, confirm the page updates without errors.

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    message = "Welcome to the Flask Web App!"
    return render_template('home.html', message=message)

@app.route('/about')
def about():
    return '<h1>About This App</h1><p>This app demonstrates a simple Flask web application with routes and form handling.</p>'

@app.route('/greet', methods=['POST'])
def greet():
    name = request.form.get('name', 'Guest')
    greeting = f'Hello, {name}! Thanks for visiting.'
    return render_template('home.html', message=greeting)

if __name__ == '__main__':
    app.run(debug=True)

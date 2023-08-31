'''
This module shows a script  that displays "Hello HBNB!" when accessing the root URL.
'''
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    This route displays "Hello HBNB!" when accessing the root URL.
    """
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    This route displays "HBNB" when accessing the '/hbnb' URL.
    """
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def custom_text(text):
    """
    This route displays "C " followed by the value of the 'text' variable.
    Replace underscore _ symbols with a space.
    """
    text = text.replace('_', ' ')
    return f"C {text}"

@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def python_text(text="is cool"):
    """
    This route displays "Python " followed by the value of the 'text' variable.
    Replace underscore _ symbols with a space. The default value of 'text' is "is cool".
    """
    text = text.replace('_', ' ')
    return f"Python {text}"

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    This route displays "<n> is a number" if n is an integer.
    """
    return f"{n} is a number"

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    This route displays an HTML page with "Number: n" in an H1 tag in the body.
    """
    return render_template('number_template.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
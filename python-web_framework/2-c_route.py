'''
This module shows a script  that displays "Hello HBNB!" when accessing the root URL.
'''

from flask import Flask

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
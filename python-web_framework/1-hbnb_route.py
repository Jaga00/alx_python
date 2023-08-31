#script that starts a Flask web application

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
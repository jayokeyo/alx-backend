#!/usr/bin/env python3
'''
Create a single / route and an index.html template that simply outputs 
“Welcome to Holberton” as page title (<title>) and “Hello world” as header (<h1>).
'''


from flask import Flask, render_template
from flask_babel import Babel


class Config() -> None:
    '''configure babel app
    '''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

@app.route('/', methods = ['GET', 'POST'], strict_slashes=False)
def index() -> str:
    '''Render index.html
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')

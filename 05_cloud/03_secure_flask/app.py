# File: app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, world!'

if __name__ == '__main__':
    app.run(port=4321, ssl_context=('./localhost+1.pem', 'localhost+1-key.pem'))

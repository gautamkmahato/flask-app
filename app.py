from flask import Flask
import os

app = Flask(__name__)

PORT = 5000

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

if __name__ == '__main__':
    app.run(debug=True)
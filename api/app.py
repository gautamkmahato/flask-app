from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>This is a flask Text to speech app</h1><p>This is test Application build using flask</p>'

@app.route('/about')
def about():
    return 'About'
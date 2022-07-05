from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/stickers')
def sticker_page():
    return render_template('stickers.html')

@app.route('/3d')
def print_page():
    return render_template('3d.html')

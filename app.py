from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/Home')
def home():
  return render_template('home.html', item_name='Tyson ,Connor, Alister O, Babe B, O.J ')

@app.route("/index")
def Favorite_page():
  return render_template('index.html')


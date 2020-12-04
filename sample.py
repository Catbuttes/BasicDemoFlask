#!/usr/env python3

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def load_initial_page():
    return render_template("file.html")

@app.route('/submit', methods=['POST'])
def handle_form_data():
    print("User: " + request.form['user'])
    print("Password: " + request.form['password'])
    return render_template("./file.html", user=request.form['user'], password=request.form['password'])

app.run()
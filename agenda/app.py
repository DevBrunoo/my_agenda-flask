import os 

from flask import Flask, render_template, flash, jsonify, redirect, render_template, request, session

app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route('/')
def homepage():
    return render_template("homepage.html")
@app.route('/contact')
def link():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
from flask import render_template, request, redirect, url_for, session, flash
from app import app

@app.route('/')
def index():
    return render_template('index.html')
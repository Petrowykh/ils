from flask import Flask
from config import Config

def create_app():
    app = Flask(__name__)
    return app

app = create_app()
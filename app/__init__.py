"""A simple flask web app"""
from flask import Flask, render_template


def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

    @app.route("/")
    def index():
        return render_template('index.html')

    @app.route("/Bdata")
    def about():
        return render_template('bigdata.html')

    @app.route("/DBMS")
    def fpat():
        return render_template('DBMS.html')

    @app.route("/python")
    def python():
        return render_template('python.html')

    @app.route("/R-prog")
    def rprog():
        return render_template('rprog.html')
    return app

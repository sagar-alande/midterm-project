"""A simple flask web app"""
from flask import Flask, render_template


def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

    @app.route("/")
    def index():
        return render_template('index.html')

    @app.route("/github")
    def about():
        return render_template('github.html')

    @app.route("/docker")
    def fpat():
        return render_template('docker.html')

    @app.route("/python")
    def python():
        return render_template('python.html')

    @app.route("/cicd")
    def rprog():
        return render_template('cicd.html')


    @app.route("/solid")
    def solid():
        return render_template('solid.html')


    @app.route("/aaa")
    def aaa():
        return render_template('aaa_test.html')
    return app

# main.py

from src import logging_config
from flask import Flask
from src import app

if __name__ == "__main__":
    app.run(debug=True, port=5001)

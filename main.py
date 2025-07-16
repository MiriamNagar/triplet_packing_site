# main.py

from src import logging_config
from flask import Flask
from src import app
# import logging_config 

if __name__ == '__main__':
    app.run(debug=True)
    # app.run(debug=True, port=5001)
    # app.run()
    # app.run(debug=True, port=os.getenv("FLASK_RUN_PORT"))
# routes.py

from flask import render_template, request
from src import app
# from .your_algorithm_module import run_algorithm  # Replace with actual import
from prtpy.packing.triplet_packing import backtrack_method, local_search
from prtpy.binners import BinnerKeepingContents
# from generate_random import create_random_allocatable_item_list
import logging, os
from .import logging_config

import inspect

def set_log_level(level_name):
    level_dict = {
        'DEBUG': logging.DEBUG,
        'INFO': logging.INFO,
        'WARNING': logging.WARNING,
        'ERROR': logging.ERROR,
        'CRITICAL': logging.CRITICAL,
    }
    log_level = level_dict.get(level_name, logging.INFO)  # default to info
    logging.getLogger().setLevel(log_level)


@app.route('/', methods=['GET', 'POST'])
def index():
    output = ""
    logs = ""
    error_message = ""

    selected_log_level = 'INFO'  # set default

    if request.method == 'POST':
        try:
            items_str = request.form['items']
            binsize = int(request.form['binsize'])
            method = str(request.form["method"])
            selected_log_level = request.form.get('log_level', 'INFO')

            set_log_level(selected_log_level)

            if not items_str:
                raise ValueError("Please enter item values.")

            items = [int(x.strip()) for x in items_str.split(',') if x.strip()]
            if any(i <= 0 for i in items) or binsize <= 0:
                raise ValueError("All numbers must be positive.")

            # Run your algorithm
            if method == "backtracking":
                output = backtrack_method(BinnerKeepingContents(), binsize, items)
            elif method == "local search":
                output = local_search(BinnerKeepingContents(), binsize, items)
            
            # read log file
            if os.path.exists('algorithm.log'):
                with open('algorithm.log', 'r') as log_file:
                    logs = log_file.read()
            else:
                logs = "No log file found. Logging might not have started yet."

        except Exception as e:
            error_message = str(e)

    # return render_template("index.html", output=output, logs=logs, error_message=error_message)
    return render_template(
        "index.html",
        output=output,
        logs=logs,
        error_message=error_message,
        selected_log_level=selected_log_level
    )


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/algorithm')
def algorithm():
    return render_template("algorithm.html")


@app.route('/how-to-use')
def how_to_use():
    return render_template("how_to_use.html")



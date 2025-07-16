# routes.py

from flask import render_template, request, redirect, url_for, session
from src import app
import prtpy
from prtpy.packing.triplet_algo.models import SolverData
import logging, os
from .logging_config import algo_logger
import io

import traceback
import inspect
import os


def set_log_level(level_name):
    level_dict = {
        'DEBUG': logging.DEBUG,
        'INFO': logging.INFO,
        'WARNING': logging.WARNING,
        'ERROR': logging.ERROR,
        'CRITICAL': logging.CRITICAL,
    }
    log_level = level_dict.get(level_name)  # default to info
    algo_logger.setLevel(log_level)


@app.route('/', methods=['GET', 'POST'])
def index():
    output = ""
    logs = ""
    error_message = ""
    selected_log_level = "INFO"

    if request.method == 'POST':
        try:
            items_str = request.form['items']
            binsize_str = request.form['binsize']
            method = str(request.form["method"])
            print(f"method: {method}")
            selected_log_level = request.form['log_level']
            print(f"Received log level from form: {selected_log_level}")

            set_log_level(selected_log_level)

            # --- Setup per-request in-memory logger ---
            log_stream = io.StringIO()
            log_handler = logging.StreamHandler(log_stream)
            log_handler.setFormatter(logging.Formatter(
                "%(asctime)s - %(levelname)s - %(module)s - %(funcName)s - %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S"
            ))
            algo_logger.addHandler(log_handler)

            # Validate items
            if not items_str.strip():
                raise ValueError("Please enter valid items.")

            item_parts = [x.strip() for x in items_str.split(',') if x.strip()]
            if not item_parts:
                raise ValueError("Please enter valid items.")

            try:
                items = [int(x) for x in item_parts]
            except ValueError:
                raise ValueError("Please enter only comma-separated positive integers like: 100, 200, 300.")

            if any(i <= 0 for i in items):
                raise ValueError("All numbers must be positive.")

            # Validate binsize now, safely
            if not binsize_str.strip():
                raise ValueError("Please enter a bin size.")

            try:
                binsize = int(binsize_str)
            except ValueError:
                raise ValueError("Bin size must be a whole number.")

            if binsize <= 0:
                raise ValueError("Bin size must be a positive number.")

            if method == "backtracking":
                output = prtpy.pack(algorithm=prtpy.packing.triplet_packing, binsize=binsize, items=items, outputtype=prtpy.out.PartitionAndSums)
            elif method == "local search":
                output = prtpy.pack(algorithm=prtpy.packing.triplet_packing, binsize=binsize, items=items, outputtype=prtpy.out.PartitionAndSums)

            # --- Retrieve logs & cleanup ---
            algo_logger.removeHandler(log_handler)
            logs = log_stream.getvalue()
            log_stream.close()

        except Exception as e:
            tb = traceback.format_exc()
            print(tb)  # Optional: still print full traceback to console for debugging

            # Default error message
            error_message = str(e) or tb

            # Custom message for SolverData.Error
            if isinstance(e, SolverData.Error):
                error_message = "No solution exists for the given items and bin size."
            elif isinstance(e.__cause__, SolverData.NoSolution):
                # In case it's wrapped inside another exception
                error_message = str(e.__cause__)

            return render_template("index.html", error_message=error_message, selected_log_level=selected_log_level, items=items_str, binsize=binsize_str)
    return render_template("index.html", output=output, logs=logs, selected_log_level=selected_log_level)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/algorithm')
def algorithm():
    return render_template("algorithm.html")


@app.route('/how-to-use')
def how_to_use():
    return render_template("how_to_use.html")

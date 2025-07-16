# routes.py

import prtpy
import logging
import io
import traceback
from flask import render_template, request
from src import app
from .logging_config import algo_logger
from prtpy.packing.triplet_algo.models import SolverData


# Utility: Set logging level
def set_log_level(level_name):
    levels = {
        "DEBUG": logging.DEBUG,
        "INFO": logging.INFO,
        "WARNING": logging.WARNING,
        "ERROR": logging.ERROR,
        "CRITICAL": logging.CRITICAL,
    }
    algo_logger.setLevel(levels.get(level_name, logging.INFO))


# Main Route: Index Page
@app.route("/", methods=["GET", "POST"])
def index():
    output = ""
    logs = ""
    error_message = ""
    selected_log_level = "INFO"

    if request.method == "POST":
        try:
            # --- Get form inputs ---
            items_str = request.form["items"]
            binsize_str = request.form["binsize"]
            method = request.form["method"]
            selected_log_level = request.form["log_level"]

            set_log_level(selected_log_level)

            # --- Setup in-memory logging stream ---
            log_stream = io.StringIO()
            log_handler = logging.StreamHandler(log_stream)
            log_handler.setFormatter(logging.Formatter(
                "%(asctime)s - %(levelname)s - %(module)s - %(funcName)s - %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S",
            ))
            algo_logger.addHandler(log_handler)

            # --- Validate & parse items ---
            if not items_str.strip():
                raise ValueError("Please enter valid items.")

            item_parts = [x.strip() for x in items_str.split(",") if x.strip()]
            if not item_parts:
                raise ValueError("Please enter valid items.")

            try:
                items = [int(x) for x in item_parts]
            except ValueError:
                raise ValueError(
                    "Please enter only comma-separated positive integers like: 100, 200, 300."
                )

            if any(i <= 0 for i in items):
                raise ValueError("All numbers must be positive.")

            # --- Validate bin size ---
            if not binsize_str.strip():
                raise ValueError("Please enter a bin size.")

            try:
                binsize = int(binsize_str)
            except ValueError:
                raise ValueError("Bin size must be a whole number.")

            if binsize <= 0:
                raise ValueError("Bin size must be a positive number.")

            # --- Run algorithm ---
            if method == "backtracking":
                output = prtpy.pack(
                    algorithm=prtpy.packing.triplet_packing,
                    binsize=binsize,
                    items=items,
                    outputtype=prtpy.out.PartitionAndSums,
                )
            elif method == "local search":
                output = prtpy.pack(
                    algorithm=prtpy.packing.triplet_packing,
                    binsize=binsize,
                    items=items,
                    outputtype=prtpy.out.PartitionAndSums,
                )

            # --- Collect logs and clean up ---
            algo_logger.removeHandler(log_handler)
            logs = log_stream.getvalue()
            log_stream.close()

        except Exception as e:
            tb = traceback.format_exc()
            algo_logger.error(tb)  # Optional: useful for console debugging

            error_message = str(e) or tb

            # Specific error messaging
            if isinstance(e, SolverData.Error):
                error_message = "No solution exists for the given items and bin size."
            elif isinstance(e.__cause__, SolverData.NoSolution):
                error_message = str(e.__cause__)

            return render_template(
                "index.html",
                error_message=error_message,
                selected_log_level=selected_log_level,
                items=items_str,
                binsize=binsize_str,
            )

    return render_template(
        "index.html",
        output=output,
        logs=logs,
        selected_log_level=selected_log_level,
    )


# Additional Pages
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/algorithm")
def algorithm():
    return render_template("algorithm.html")


@app.route("/how-to-use")
def how_to_use():
    return render_template("how_to_use.html")

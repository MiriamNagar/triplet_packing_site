# routes.py

from flask import Blueprint, render_template, request
from your_algorithm_module import run_algorithm  # Replace with actual import

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    output = ""
    logs = ""
    error_message = ""

    if request.method == 'POST':
        try:
            items_str = request.form['items']
            binsize = int(request.form['binsize'])

            if not items_str:
                raise ValueError("Please enter item values.")

            items = [int(x.strip()) for x in items_str.split(',') if x.strip()]
            if any(i <= 0 for i in items) or binsize <= 0:
                raise ValueError("All numbers must be positive.")

            # Run your algorithm
            output, logs = run_algorithm(items, binsize)

        except Exception as e:
            error_message = str(e)

    return render_template("index.html", output=output, logs=logs, error_message=error_message)


@main.route('/about')
def about():
    return render_template("about.html")


@main.route('/algorithm')
def algorithm():
    return render_template("algorithm.html")


@main.route('/how-to-use')
def how_to_use():
    return render_template("how_to_use.html")

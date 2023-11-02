from flask import Flask, render_template
from interface.get_issue_types import get_issue_type_names_for_dropdown
from output.create_html import create_table_body_string
app = Flask(__name__)


@app.route('/')
def home():
    issue_types = get_issue_type_names_for_dropdown()
    # print('issue_types', issue_types)
    return render_template(
        "index.html",
        issue_types=issue_types,
    )


@app.route("/results/<issue_type>")
def results(issue_type=None):
    """Creates endpoint for showing issues from search in HTML
    table format or, if do_export is True, creates spreadsheet and
    returns it
    """
    driver_array_for_table = [
        ['row1data', '123', '456'],
        ['row2data', '789', '10-11-12']
    ]
    # expected_table_body_string = '<table><tbody><tr><td>row1 data</td><td>123</td><td>456</td></tr><tr><td>row2 data</td><td>789</td><td>10-11-12</td></tr>'

    results_table = create_table_body_string(driver_array_for_table)
    # results_table = []
    return render_template(
        "results.html",
        results_table=results_table
    )


if __name__ == '__main__':
    app.run(debug=True)

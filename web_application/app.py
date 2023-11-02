""" Main entry point for Flask application, with endpoints defined """
import json
from flask import Flask, render_template, send_file
from output.create_html import get_table_from_results

app = Flask(__name__)

# keep
@app.route("/")
def home():
    """Creates entry endpoint, displays search form(s)
    """
    return render_template(
        "index.html",
        # issuetypes=json.dumps(get_issue_type_list()),
        # statuses=json.dumps(get_statuses_for_dropdown()),
        # boards=json.dumps(get_sls_boards()),
        # sprints=json.dumps(get_sprints_for_dropdown()),
    )

# SET UP ROUTES
@app.route("/test")
def test():
    """Test endpoint
    """
    return "Flask is running!"

# <do_export> is an optional URL parameter
# @app.route("/results/<version>/<issuetype>/<status>", defaults={'do_export': False})
# @app.route("/results/<version>/<issuetype>/<status>/<do_export>")
# def results(version, issuetype, status, do_export):
#     """Creates endpoint for showing results of Epics with
#     associated issues in HTML table format"""
#     results_array = get_arrays_from_search(version, issuetype, status)
#     if len(results_array) == 0:
#         return render_template("no_results.html")
#     results_table = json.dumps(get_table_from_results(results_array))
#     if do_export == 'export':
#         output = create_ss_w_pandas([
#             ['Type', 'Key', 'Summary', 'Epic Link', 'Current Status', 'Related Sprint'], *results_array],
#             'epicreport'
#         )
#         return send_file(output, download_name=create_epic_filename(), as_attachment=True)
#     export_url="/results/"+version+"/"+issuetype+"/"+status+"/export"
#     return render_template("results.html", results_table=results_table, export_url=export_url)


# @app.route("/sprintmetrics/<sprint_id>", defaults={'do_export': False})
# @app.route("/sprintmetrics/<sprint_id>/<do_export>")
# def sprintmetrics(sprint_id, do_export):
#     """Creates endpoint for displaying sprint metrics table"""
#     results_array = get_issues_for_sprint(sprint_id)
#     if len(results_array) == 0:
#         return render_template("no_results.html")
#     sprint_metrics_table = json.dumps(
#         get_table_from_sprint_metrics(results_array)
#     )
#     if do_export == 'export':
#         output = create_ss_w_pandas(results_array, 'sprintreport')
#         return send_file(output, download_name=create_sprint_filename(), as_attachment=True)
    
#     export_url="/sprintmetrics/"+sprint_id+"/export"
#     return render_template(
#         "sprint_metrics.html", sprint_metrics_table=sprint_metrics_table, export_url=export_url
#     )
    
if __name__ == "__main__":
    app.run(port=5000, debug=True)

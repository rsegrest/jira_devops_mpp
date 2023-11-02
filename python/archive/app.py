""" Main entry point for Flask application, with endpoints defined """
import json
from flask import Flask, render_template, send_file
from interface.get_issue_types import get_issue_types

app = Flask(__name__)

# keep
@app.route("/")
def home():
    """Creates entry endpoint, displays search form(s)
    """
    return render_template(
        "index.html",
        issuetypes=json.dumps(get_issue_types()),
    )

# SET UP ROUTES
@app.route("/test")
def test():
    """Test endpoint
    """
    return "Flask is running!"

if __name__ == "__main__":
    app.run(port=5000, debug=True)

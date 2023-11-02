from atlassian import Jira
import time
from auth.read_token import read_token

# Get the SSL certificate files
# CERT_FILE = './static_data/bundle.pem'

token = read_token()

def connect_to_jira():
    """Connects to the Jira API, and returns the connection obj"""
    jira = Jira(
        url="http://host.docker.internal:8080",
        token=token,
        # url='https://jira-gc.nasa.gov',
        # verify_ssl=CERT_FILE
    )
    return jira



""" Methods to connect to and interface with Jira API """
from interface.connect import connect_to_jira
from auth.read_token import read_token

token = read_token()

def get_issue_types():
    jira = connect_to_jira()
    issue_types = jira.get_issue_types()
    mapped_issue_types = map(
        lambda x: x['name'],
        issue_types
    )
    return ['ALL', *list(mapped_issue_types)]
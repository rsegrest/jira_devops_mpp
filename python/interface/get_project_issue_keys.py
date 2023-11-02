# Get all project issue keys.
# JIRA Cloud API can return up to  100 results  in one API call.
# If your project has more than 100 issues see following community discussion:
# https://community.atlassian.com/t5/Jira-Software-questions/Is-there-a-limit-to-the-number-of-quot-items-quot-returned-from/qaq-p/1317195

""" Methods to connect to and interface with Jira API """
from interface.connect import connect_to_jira
from auth.read_token import read_token

token = read_token()

def get_project_issue_keys(project="MPPSAM"):
    jira = connect_to_jira()
    issuekeys = jira.get_project_issuekey_all(project)
    # values = fields['values']
    # mapped_values = map(lambda x: {'id': x['id'], 'name': x['name']}, values)
    # return list(mapped_values)
    return issuekeys
issue_keys = get_project_issue_keys()
print(issue_keys)